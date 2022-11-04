#!/bin/bash
data_dir=$1
save_dir=$2

python -u scripts/osse_2020a/nerf/preprocess/pre_swotnadir.py \
    --dir_obs=$data_dir \
    --dir_obs_save=$save_dir