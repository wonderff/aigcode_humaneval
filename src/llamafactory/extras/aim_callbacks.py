import asyncio
from logging import getLogger
from typing import Optional, List, Dict
from difflib import SequenceMatcher
import time
from collections import defaultdict

ENABLE_AIM = True
try:
    from aim.ext.resource.configs import DEFAULT_SYSTEM_TRACKING_INT
    from aim.sdk.num_utils import is_number
    from aim.sdk.run import Run
except ImportError:
    ENABLE_AIM = False

try:
    from transformers.trainer_callback import TrainerCallback
except ImportError:
    raise RuntimeError(
        'This contrib module requires Transformers to be installed. '
        'Please install it with command: \n pip install transformers'
    )

logger = getLogger(__name__)

class AimCallback(TrainerCallback):
    def __init__(
        self,
        repo: Optional[str] = None,
        experiment: Optional[str] = None,
        system_tracking_interval: Optional[int] = DEFAULT_SYSTEM_TRACKING_INT,
        log_system_params: Optional[bool] = True,
        capture_terminal_logs: Optional[bool] = True,
    ):
        self._repo_path = repo
        self._experiment_name = experiment
        self._system_tracking_interval = system_tracking_interval
        self._log_system_params = log_system_params
        self._capture_terminal_logs = capture_terminal_logs
        self._run = None
        self._run_hash = None
        self._log_value_warned = False
        self._step_start_time = None

    @property
    def experiment(self):
        if not self._run:
            asyncio.create_task(self.setup())
        return self._run

    async def setup(self, args=None, state=None, model=None):
        global ENABLE_AIM
        if state and not state.is_world_process_zero:
            return

        if not ENABLE_AIM:
            return

        try:
            if not self._run:
                if self._run_hash:
                    self._run = Run(
                        self._run_hash,
                        repo=self._repo_path,
                        system_tracking_interval=self._system_tracking_interval,
                        capture_terminal_logs=self._capture_terminal_logs,
                    )
                else:
                    self._run = Run(
                        repo=self._repo_path,
                        experiment=self._experiment_name,
                        system_tracking_interval=self._system_tracking_interval,
                        log_system_params=self._log_system_params,
                        capture_terminal_logs=self._capture_terminal_logs,
                    )
                    self._run_hash = self._run.hash

            if args:
                combined_dict = {**args.to_sanitized_dict()}
                for key, value in combined_dict.items():
                    await self.async_set_run(('hparams', key), value)
            if model:
                await self.async_set_run('model', {**vars(model.config), 'num_labels': getattr(model, 'num_labels', None)})
        except Exception as e:
            ENABLE_AIM = False
            logger.error(f"Error in setup: {e}")

    async def async_set_run(self, key, value):
        global ENABLE_AIM
        if not ENABLE_AIM:
            return
        p = enumerate()
        try:
            self._run.set(key, value, strict=False)
        except Exception as e:
            ENABLE_AIM = False
            logger.error(f"Error setting run value for {key}: {e}")

    def on_init_end(self, args, state, control, **kwargs):
        if not ENABLE_AIM:
            return
        asyncio.create_task(self.setup(state=state))

    def on_train_begin(self, args, state, control, model=None, **kwargs):
        if not ENABLE_AIM:
            return
        self._step_start_time = time.time()
        asyncio.create_task(self.setup(args, state, model))

    def on_step_end(self, args, state, control, **kwargs):
        if not state.is_world_process_zero or not ENABLE_AIM:
            return

        step_duration = time.time() - self._step_start_time
        self._step_start_time = time.time()

        remaining_steps = state.max_steps - state.global_step
        estimated_remaining_time = remaining_steps * step_duration

        values_to_set = {
            'estimated_remaining_time': estimated_remaining_time,
            'max_steps': state.max_steps,
            'global_step': state.global_step
        }

        asyncio.create_task(self.async_set_multiple_runs(values_to_set))

    def on_train_end(self, args, state, control, **kwargs):
        if not ENABLE_AIM:
            return
        asyncio.create_task(self.async_set_run('estimated_remaining_time', 0.0))
        if not state.is_world_process_zero:
            return
        asyncio.create_task(self.async_close())

    def on_log(self, args, state, control, model=None, logs=None, **kwargs):
        if not state.is_world_process_zero or not ENABLE_AIM:
            return

        if not self._run:
            asyncio.create_task(self.setup(args, state, model))

        tasks = []
        for log_name, log_value in logs.items():
            context = {}
            prefix_set = {'train_', 'eval_', 'test_'}
            for prefix in prefix_set:
                if log_name.startswith(prefix):
                    log_name = log_name[len(prefix):]
                    context = {'subset': prefix[:-1]}
                    if '_' in log_name:
                        sub_dataset = AimCallback.find_most_common_substring(
                            list(logs.keys())
                        ).split(prefix)[-1]
                        if sub_dataset != prefix.rstrip('_'):
                            log_name = log_name.split(sub_dataset)[-1].lstrip('_')
                            context['sub_dataset'] = sub_dataset
                    break
            if not is_number(log_value):
                if not self._log_value_warned:
                    self._log_value_warned = True
                    logger.warning(
                        f'Trainer is attempting to log a value of '
                        f'"{log_value}" of type {type(log_value)} for key "{log_name}"'
                        f' as a metric which is not a supported value type.'
                    )
                continue

            tasks.append(self.async_track(log_value, log_name, context, state.global_step, state.epoch))

        if tasks:
            asyncio.create_task(asyncio.gather(*tasks))

    async def async_track(self, value, name, context, step, epoch):
        global ENABLE_AIM
        if not ENABLE_AIM:
            return

        try:
            self._run.track(value, name=name, context=context, step=step, epoch=epoch)
        except Exception as e:
            ENABLE_AIM = False
            logger.error(f"Error tracking value {name}: {e}")

    async def async_set_multiple_runs(self, values: Dict[str, any]):
        global ENABLE_AIM
        if not ENABLE_AIM:
            return

        try:
            for key, value in values.items():
                await self.async_set_run(key, value)
        except Exception as e:
            ENABLE_AIM = False
            logger.error(f"Error setting multiple run values: {e}")

    async def async_close(self):
        global ENABLE_AIM
        if not ENABLE_AIM:
            return

        try:
            if self._run:
                self._run.close()
                del self._run
                self._run = None
        except Exception as e:
            ENABLE_AIM = False
            logger.error(f"Error closing run: {e}")

    @staticmethod
    def find_most_common_substring(names: List[str]) -> str:
        substring_counts = defaultdict(lambda: 0)

        for i in range(0, len(names)):
            for j in range(i + 1, len(names)):
                string1 = names[i]
                string2 = names[j]
                match = SequenceMatcher(None, string1, string2).find_longest_match(
                    0, len(string1), 0, len(string2)
                )
                matching_substring = string1[match.a:match.a + match.size]
                substring_counts[matching_substring] += 1

        return max(substring_counts, key=lambda x: substring_counts[x]).rstrip('_')

    def __del__(self):
        asyncio.create_task(self.async_close())