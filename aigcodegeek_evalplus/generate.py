import os
from os import PathLike
from typing import List

from model import DecoderBase, make_model
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
)


def codegen(
    workdir: PathLike,
    model: DecoderBase,
    dataset: str,
    greedy=False,
    n_samples=1,
    id_range=None,
    resume=True,
):
    with Progress(
        TextColumn(f"{dataset} •" + "[progress.percentage]{task.percentage:>3.0f}%"),
        BarColumn(),
        MofNCompleteColumn(),
        TextColumn("•"),
        TimeElapsedColumn(),
    ) as p:
        if dataset == "humaneval":
            from evalplus.data import get_human_eval_plus

            dataset = get_human_eval_plus()
        elif dataset == "mbpp":
            from evalplus.data import get_mbpp_plus

            dataset = get_mbpp_plus()

        for task_id, task in p.track(dataset.items()):
            if id_range is not None:
                id_num = int(task_id.split("/")[1])
                low, high = id_range
                if id_num < low or id_num >= high:
                    p.console.print(f"Skipping {task_id} as it is not in {id_range}")
                    continue

            p_name = task_id.replace("/", "_")
            os.makedirs(os.path.join(workdir, p_name), exist_ok=True)
            log = f"Codegen: {p_name} @ {model}"
            n_existing = 0
            if resume:
                # count existing .py files
                n_existing = len(
                    [
                        f
                        for f in os.listdir(os.path.join(workdir, p_name))
                        if f.endswith(".py")
                    ]
                )
                if n_existing > 0:
                    log += f" (resuming from {n_existing})"

            nsamples = n_samples - n_existing
            # p.console.print(log)

            sidx = n_samples - nsamples
            while sidx < n_samples:
                outputs = model.codegen(
                    task["prompt"].strip(),
                    do_sample=not greedy,
                    num_samples=n_samples - sidx,
                )
                assert outputs, "No outputs from model!"
                for impl in outputs:
                    try:
                        with open(
                            os.path.join(workdir, p_name, f"{sidx}.py"),
                            "w",
                            encoding="utf-8",
                        ) as f:
                            if model.direct_completion and False:
                                f.write(task["prompt"] + impl)
                            else:
                                f.write(impl)
                    except UnicodeEncodeError:
                        continue
                    sidx += 1

models = {
    'aigcode': {
        'v1': "aigcode/AIGCodeGeek-DS-6.7B"
    }
}
templates = {
    'v1': "AIGCodeGeek",
}

def get_eval_config(model_series: str, release_tag: str) -> (str, str):
    #assert model_series in models, f"Unsupported models {model_series}"
    #assert release_tag in templates, f"Unsupported templates {release_tag}"
    model_path = model_series #models[model_series][release_tag]
    eval_template = templates[release_tag]
    return model_path, eval_template

def main(
    model_series: str,
    release_tag: str,
    dataset: str,
    root: str,
    bs: int = 1,
    n_samples: int = 1,
    temperature: float = 0.0,
    resume: bool = True,
    greedy: bool = True,
    id_range: List = None,
    tp: int = 1,
):
    assert dataset in ["humaneval", "mbpp"], f"Invalid dataset {dataset}"

    if greedy and (temperature != 0 or bs != 1 or n_samples != 1):
        temperature = 0
        bs = 1
        n_samples = 1
        print("Greedy decoding ON (--greedy): setting bs=1, n_samples=1, temperature=0")


    if id_range is not None:
        assert len(id_range) == 2, "id_range must be a list of length 2"
        assert id_range[0] < id_range[1], "id_range must be increasing"
        id_range = tuple(id_range)

    # Make project dir
    os.makedirs(root, exist_ok=True)
    # Make dataset dir
    os.makedirs(os.path.join(root, dataset), exist_ok=True)
    # Make dir for codes generated by each model

    model_id, template = get_eval_config(model_series, release_tag)
    model_runner = make_model(
        model=model_id,
        template=template, 
        batch_size=bs,
        temperature=temperature,
        dataset=dataset,
        # tp=tp,
    )
    identifier = model_id.replace("/", "_") + f"_temp_{temperature}"
    workdir = os.path.join(root, dataset, identifier)
    os.makedirs(workdir, exist_ok=True)
    codegen(
        workdir=workdir,
        dataset=dataset,
        greedy=greedy,
        model=model_runner,
        n_samples=n_samples,
        resume=resume,
        id_range=id_range,
    )


if __name__ == "__main__":
    from fire import Fire

    Fire(main)                    