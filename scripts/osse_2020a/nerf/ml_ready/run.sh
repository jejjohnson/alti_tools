#!/bin/bash
data_dir=$1
save_dir=$2


# NADIR 1
python -u scripts/osse_2020a/nerf/ml_ready/ml_swotnadir.py \
    --my_config=scripts/osse_2020a/nerf/ml_ready/config.py \
    --setup=nadir1 \
    --dataset_dir=$1 \
    --save_dir=$2

# NADIR 4
python -u scripts/osse_2020a/nerf/ml_ready/ml_swotnadir.py \
    --my_config=scripts/osse_2020a/nerf/ml_ready/config.py \
    --setup=nadir4 \
    --dataset_dir=$1 \
    --save_dir=$2

# SWOT 1 NADIR 1
python -u scripts/osse_2020a/nerf/ml_ready/ml_swotnadir.py \
    --my_config=scripts/osse_2020a/nerf/ml_ready/config.py \
    --setup=swot1nadir1 \
    --dataset_dir=$1 \
    --save_dir=$2

# SWOT 1 NADIR 5
python -u scripts/osse_2020a/nerf/ml_ready/ml_swotnadir.py \
    --my_config=scripts/osse_2020a/nerf/ml_ready/config.py \
    --setup=swot1nadir5 \
    --dataset_dir=$1 \
    --save_dir=$2