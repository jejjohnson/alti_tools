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
from loguru import logger
import time

from alti_tools._src.data.osse import check_osse_files

# Altitools
from alti_tools._src.data.ssh import download_ssh_toy
from alti_tools._src.transforms import spatial, temporal
from alti_tools._src.viz import psd as psd_plots
from alti_tools._src.preprocess.swot import preprocess_karin_swot
from alti_tools._src.utils.tracking import get_current_timestamp
from alti_tools._src.utils.files import list_all_files, check_list_equal_elem
from alti_tools._src.utils.files import check_if_directory, check_if_file
from alti_tools._src.data.configs.altimetry import (
    get_raw_altimetry_config,
    get_raw_altimetry_files,
)
from alti_tools._src.data.swot import load_alongtrack_parallel

FLAGS = flags.FLAGS

# config_flags.DEFINE_config_file("my_config")
flags.DEFINE_string("dir_obs", str(root.joinpath("datasets")), "the experimental")
flags.DEFINE_string(
    "dir_obs_save",
    str(root.joinpath("datasets")),
    "the experimental",
)


def main(_):
    logger.info("Starting preprocessing script...")
    t0 = time.time()

    # check the psuedo-obs files
    logger.info("checking files...")
    check_osse_files(FLAGS.dir_obs, None, "obs")

    # correct file types for datasets
    logger.info("Get NADIR track files...")
    obs_files = get_raw_altimetry_files(FLAGS.dir_obs, "nadir")

    # load them in parallel
    logger.info("Load NADIR tracks (parallel)...")
    ds_nadir = load_alongtrack_parallel(obs_files)

    logger.debug("Checking size of nadir data...")
    assert ds_nadir.coords["time"].shape == (205232,)

    logger.info("Get SWOT track files...")
    file_path = get_raw_altimetry_files(FLAGS.dir_obs, "swot")

    logger.info("Open KARIN SWOT dataset...")
    ds_swot_karin = xr.open_dataset(file_path[0])

    logger.info("Preprocess KARIN SWOT dataset...")
    ds_swot_karin = preprocess_karin_swot(ds_swot_karin, author="Emmanuel")

    logger.debug("Checking size of swot data...")
    assert ds_swot_karin.coords["time"].shape == (8_412_216,)

    # SWOT NADIR DATA
    logger.info("Get SWOT track files...")
    file_path = get_raw_altimetry_files(FLAGS.dir_obs, "swotnadir")

    logger.info("Open KARIN SWOT NADIR dataset...")
    ds_nadir_swot = xr.open_dataset(file_path[0])

    # select the first cycle
    ds_nadir_swot = ds_nadir_swot.isel(cycle=0)

    logger.debug("Checking size of swot nadir data...")
    assert ds_nadir_swot.coords["time"].shape == (161_333,)

    # COMBINED DATASET
    variables = ["ssh_obs", "ssh_model", "lon", "lat"]

    ds_swot = xr.concat(
        [ds_nadir_swot[variables], ds_swot_karin[variables]],
        dim="time",
        data_vars=variables,
        coords=["time"],
    )
    # sort by time
    ds_swot = ds_swot.sortby("time")

    logger.info("Checking size of full combined dataset...")
    assert ds_swot.coords["time"].shape == (8573549,)

    # FULLY COMBINED DATASET

    ds_swot_nadir = xr.concat(
        [ds_swot[variables], ds_nadir[variables]],
        dim="time",
        data_vars=variables,
        coords=["time"],
    )
    # sort by time
    ds_swot_nadir = ds_swot_nadir.sortby("time")

    assert ds_swot_nadir.coords["time"].shape == (205_232 + 8_412_216 + 161_333,)

    logger.info(f"Saving NADIR SWOT observation data to:")
    logger.info(f"{FLAGS.dir_obs_save}")
    ds_swot_nadir.to_netcdf(FLAGS.dir_obs_save)

    logger.info(f"Done!")
    logger.debug(f"Time Taken: {time.time()-t0:.2f} secs")


if __name__ == "__main__":
    app.run(main)
