mkdir -p results/mbpp



#!/bin/bash
# Define and process checkpoints from 6000 to 10100, every 100
for checkpoint in $(seq 7200 -100 7200); do
  python3 generate.py \
    --model_series /sharedata/saves/deepseek-ai/deepseek-coder-6.7b-base/full/train_2024-06-09-02-16-12/checkpoint-${checkpoint} \
    --release_tag v1 \
    --dataset mbpp \
    --root generations \
    --greedy True
  echo evalplus.evaluate \
    --dataset mbpp \
    --samples generations/mbpp/_sharedata_saves_deepseek-ai_deepseek-coder-6.7b-base_full_train_2024-06-09-02-16-12_checkpoint-${checkpoint}_temp_0.0 \> results/mbpp/aigcodev1_temp_0.0_checkpoint-${checkpoint}.txt
  evalplus.evaluate \
    --dataset mbpp \
    --samples generations/mbpp/_sharedata_saves_deepseek-ai_deepseek-coder-6.7b-base_full_train_2024-06-09-02-16-12_checkpoint-${checkpoint}_temp_0.0 > results/mbpp/aigcodev1_temp_0.0_checkpoint-${checkpoint}.txt
done

