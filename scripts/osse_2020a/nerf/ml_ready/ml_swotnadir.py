"""
* Check the folders
* Load Data Individually From Folders (NADIR,)
* 
"""
import os
import sys

from pyprojroot import here

# spyder up to find the root
root = here(project_files=[".root"])

# append to path
sys.path.append(str(root))
import xarray as xr
from absl import app, flags
from ml_collections import config_flags
from loguru import logger
import time
from pathlib import Path


from alti_tools._src.data.natl60.osse import check_osse_files
from alti_tools._src.preprocess.swot import preprocess_karin_swot
from alti_tools._src.data.configs.altimetry import get_raw_altimetry_files
from alti_tools._src.data.io import load_xr_datasets_list
from alti_tools._src.utils.files import list_all_files
from alti_tools._src.data.natl60.osse import get_swot_obs_setup_files
from alti_tools._src.preprocess.spatial import (
    correct_longitude,
    subset_spatial,
)
from alti_tools._src.preprocess.temporal import subset_temporal
from alti_tools._src.data.io import load_alongtrack_parallel

# TODO: Make Check and/or make directories

FLAGS = flags.FLAGS

config_flags.DEFINE_config_file("my_config")
flags.DEFINE_string("setup", "nadir1", "The experimental setup.")
flags.DEFINE_string(
    "dataset_dir", str(root.joinpath("datasets")), "the directory with the datasets"
)
flags.DEFINE_string("save_dir", str(root.joinpath("datasets")), "the save directory")


def main(_):
    logger.info("Starting preprocessing script...")
    logger.info(f"Setup: {FLAGS.setup}...")
    t0 = time.time()

    # ============================
    # LOAD DATA
    # ============================
    # get all files in directory

    logger.info("Getting files in directory...")
    all_files = list_all_files(FLAGS.dataset_dir)

    # get files required for the observations setup
    setup = "swot1nadir4"
    logger.info(f"Loading files setup: '{setup}'...")
    setup_files = get_swot_obs_setup_files(all_files, setup=FLAGS.setup)

    # choose the variables we want to open
    variables = ["ssh_obs", "ssh_model", "lon", "lat"]

    def preprocess(x):
        # subset variables
        x = x[variables]

        # subset region
        x = subset_temporal(x, FLAGS.my_config.subset)

        # correct longitude dimensions
        x = correct_longitude(x)

        # subset temporal region
        x = subset_spatial(x, FLAGS.my_config.subset)

        return x

    logger.info("Loading preprocessing script...")
    ds_swot = load_alongtrack_parallel(setup_files, preprocess=preprocess)

    # sort by time
    logger.info("Sorting by time...")
    ds_swot = ds_swot.sortby("time").compute()

    logger.info("Saving data...")
    save_name = Path(FLAGS.save_dir).joinpath(f"{FLAGS.setup}.nc")
    ds_swot.to_netcdf(save_name)

    logger.info(f"Done!")
    logger.debug(f"Time Taken: {time.time()-t0:.2f} secs")


if __name__ == "__main__":
    app.run(main)
