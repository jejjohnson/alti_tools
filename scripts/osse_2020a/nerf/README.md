
## NERF Dataset


**Downloading**

```bash
bash scripts/osse_2020a/data/dc20a_osse.sh /Volumes/EMANS_HDD/data/dc20a_osse/test/raw
```

**Preprocessing**

```bash
bash scripts/osse_2020a/nerf/preprocess/run.sh /Volumes/EMANS_HDD/data/dc20a_osse/test/raw/dc_obs /Volumes/EMANS_HDD/data/dc20a_osse/test/preprocess/osse_2020a_natl60
```

**ML Ready Preprocessing**

```bash
bash scripts/osse_2020a/nerf/ml_ready/run.sh /Volumes/EMANS_HDD/data/dc20a_osse/test/preprocess/ /Volumes/EMANS_HDD/data/dc20a_osse/test/ml
```

---
## SWOT ALTIMETRY


```bash
python -u scripts/preprocess/swot_altimetry.py \
    --dir_obs=/Volumes/EMANS_HDD/data/dc20a_osse/raw/dc_obs \
    --dir_obs_save=/Volumes/EMANS_HDD/data/dc20a_osse/test/preprocess/ds_obs_swot.nc
```

### OSSE 2020a Data Challenge 


**Downloading Data** [**TODO**]


#### Coordinate-Based Workflow

**ML NERF**:

```python
python -u scripts/preprocess/ml_nerf/osse_2020a.py \
    --my_config=scripts/preprocess/ml_nerf/config.py \
    --setup=nadir1 \
    --dataset_dir=/Volumes/EMANS_HDD/data/dc20a_osse/test/preprocess/osse_2020a_natl60/ \
    --save_dir=/Volumes/EMANS_HDD/data/dc20a_osse/test/ml
```


**Preprocessing Data**: NADIR Tracks (Eval Period)

> This script will preprocess the SWOT and NADIR tracks to have the same sizes for easy concatenation.

```bash
python -u scripts/preprocess/osse_2020a.py \
    --dir_obs=/Volumes/EMANS_HDD/data/dc20a_osse/raw/dc_obs \
    --dir_obs_save=/Volumes/EMANS_HDD/data/dc20a_osse/test/preprocess/osse_2020a_natl60
```

**Preprocessing Data**: NADIR Tracks (Simulation Period)

**Preprocessing Data**: Simulations Tracks

**ML Ready** [**TODO**]

> This script will further preprocess the data to be simplistic and ready for the PyTorch (or TensorFlow) datasets and dataloaders.

**Postprocessing** [**TODO**]

> This script will take a result a result and do the appropriate conversion and metrics to be ready for visualization.

**Viz** [**TODO**]


#### Grid-Based Workflow


**Preprocessing Data** (Grid) [**TODO**]

> This script will preprocess the SWOT and NADIR tracks to be on a predefined grid based on a specified resolution. This will allow one to concatenate all of the datasets easily.


