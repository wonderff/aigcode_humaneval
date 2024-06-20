#!/bin/bash
# Define and process checkpoints from 6000 to 10100, every 100
for checkpoint in $(seq 4400 -100 100); do

   /usr/bin/python3 generate.py \
    --model_series /sharedata/saves/deepseek-ai/deepseek-coder-6.7b-base/full/dp67full2/checkpoint-${checkpoint} \
    --release_tag v1 \
    --dataset humaneval \
    --root generations \
    --greedy True
  echo evalplus.evaluate \
    --dataset humaneval \
    --samples generations/humaneval/_sharedata_saves_deepseek-ai_deepseek-coder-6.7b-base_full_dp67full2_checkpoint-${checkpoint}_temp_0.0 \> results/humaneval/aigcodev1_temp_0.0_checkpoint-${checkpoint}.txt
  evalplus.evaluate \
    --dataset humaneval \
    --samples generations/humaneval/_sharedata_saves_deepseek-ai_deepseek-coder-6.7b-base_full_dp67full2_checkpoint-${checkpoint}_temp_0.0 > results/humaneval/aigcodev1_temp_0.0_checkpoint-${checkpoint}.txt


done

