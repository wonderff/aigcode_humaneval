import json
import os
from abc import ABC, abstractmethod
from typing import List
from warnings import warn
from transformers import AutoTokenizer, AutoModelForCausalLM
from torch_npu.contrib import transfer_to_npu
os.environ["HF_HOME"] = os.environ.get("HF_HOME", "./hf_home")
import re
import torch

EOS = [
    "<|endoftext|>",
    "<|endofmask|>",
    "</s>",
    "\nif __name__",
    "\ndef main(",
    "\nprint(",
]

class DecoderBase(ABC):
    def __init__(
        self,
        name: str,
        batch_size: int = 1,
        temperature: float = 0.8,
        max_new_tokens: int = 512,
        direct_completion: bool = True,
        dtype: str = "bfloat16",  # default
        trust_remote_code: bool = False,
        dataset: str = None
    ) -> None:
        print("Initializing a decoder model: {} ...".format(name))
        self.name = name
        self.batch_size = batch_size
        self.temperature = temperature
        self.eos = EOS
        self.direct_completion = direct_completion
        self.skip_special_tokens = False
        self.max_new_tokens = max_new_tokens
        self.dtype = dtype
        self.trust_remote_code = trust_remote_code

        if direct_completion:
            if dataset.lower() == "humaneval":
                self.eos += ["\ndef", "\nclass ", "\nimport ", "\nfrom ", "\nassert "]
            elif dataset.lower() == "mbpp":
                self.eos += ['\n"""', "\nassert"]

    @abstractmethod
    def codegen(
        self, prompt: str, do_sample: bool = True, num_samples: int = 200
    ) -> List[str]:
        pass

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

from transformers import pipeline

class TransformersDecoder(DecoderBase):
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(name, **kwargs)
        self.tokenizer = AutoTokenizer.from_pretrained(name)
        self.model = AutoModelForCausalLM.from_pretrained(name,device_map="auto")

        # self.model, self.optimizer, _, _ = deepspeed.initialize(
        #     model=self.model,
        #     model_parameters=self.model.parameters(),
        #     config='/sharedata/ben/LLaMA-Factory2/ds_z3_config.json'
        # )


    def codegen(self, prompt: str, do_sample: bool = True, num_samples: int = 200) -> List[str]:
        if do_sample:
            assert self.temperature > 0, "Temperature must be greater than 0!"
        batch_size = min(self.batch_size, num_samples)
        print(f"prompt: >>>>>>>>>>>>>>>>>>>>>>{prompt}\n<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")
        inputs = self.tokenizer([prompt]* batch_size , return_tensors="pt", padding=True, truncation=True).to("cuda")
        print("Generating text with the following parameters:")
        print(f"max_length: {self.max_new_tokens}")
        print(f"temperature: {self.temperature}")
        print(f"num_return_sequences: {batch_size}")
        print(f"do_sample: {do_sample}")
        print(f"top_p: {0.95 if do_sample else 1.0}")
        print(f"eos_token_id: {self.tokenizer.eos_token_id}")
        outputs = self.model.generate(
                        inputs.input_ids,
                        max_length=self.max_new_tokens,
                        temperature=self.temperature,
                        num_return_sequences=batch_size,
                        do_sample=do_sample,
                        top_p=0.95 if do_sample else 1.0,
                        eos_token_id=self.tokenizer.eos_token_id,
        )           

        # outputs = outputs[:, input.input_ids.shape[1]:]
        # gen_strs = [self.tokenizer.decode(outputs[i], skip_special_tokens=True)[len(prompt):-3].replace("\t", "    ") for i in range(len(outputs))
        #gen_strs = [re.search(r'```python\n(.+(\n)?)*\n```',self.tokenizer.decode(output, skip_special_tokens=True)).group(1).replace("\t", "    ") for output in outputs]
        def process_output(output):
            decoded_output = self.tokenizer.decode(output, skip_special_tokens=True)
            print(f"Decoded output: {decoded_output}")
            match = list(re.finditer(r'```python\n(.*?)(\n)?```', decoded_output, re.DOTALL))
            if len(match) > 1:
                code_block = match[1].group(1).replace("\t", "    ")
                print(f"Matched code block: {code_block}")
                return code_block
            else:
                print("No match found")
                return ""
        gen_strs = [process_output(output) for output in outputs]

        # gen_strs =  [output[len(input_str):] if output.startswith(input_str) else output  for input_str, output in zip(inputs, outputs)]
        print(gen_strs)
        print("######=========================================================================================################")
        return gen_strs



class AIGCodeGeek(TransformersDecoder):
    def __init__(self, name: str, **kwargs) -> None:
        kwargs["direct_completion"] = True
        super().__init__(name, **kwargs)
        self.eos += ["\n```"]
    def codegen(
        self, prompt: str, do_sample: bool = True, num_samples: int = 200
        ) -> List[str]:
        prompt = f"""You are an AI programming assistant, finetuned on the Deepseek Coder base model by AIGCode. You are always willing to answer code-related questions or giving accurate solutions to user instructions.
### Instruction
Write a solution to the following problem:
```python
{prompt}
```
### Response
```python
{prompt}"""
        return TransformersDecoder.codegen(self, prompt, do_sample, num_samples)




def make_model(
    model: str,
    template: str,
    dataset: str,
    batch_size: int = 1,
    temperature: float = 0.0,
    # tp=1
):
    assert template in ['AIGCodeGeek'], f"Unsupportede template {template}"
    Bot = eval(template)
    return Bot(
        name=model,
        batch_size=batch_size,
        temperature=temperature,
        max_new_tokens=1024,
        dataset=dataset,
     #    tp=tp
    )