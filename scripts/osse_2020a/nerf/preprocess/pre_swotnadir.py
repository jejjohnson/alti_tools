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
from pathlib import Path


from alti_tools._src.data.natl60.osse import check_osse_files
from alti_tools._src.preprocess.swot import preprocess_karin_swot
from alti_tools._src.data.configs.altimetry import get_raw_altimetry_files
from alti_tools._src.data.io import load_xr_datasets_list

# TODO: Make Check and/or make directories

FLAGS = flags.FLAGS

# config_flags.DEFINE_config_file("my_config")
flags.DEFINE_string("dir_obs", str(root.joinpath("datasets")), "the experimental")
flags.DEFINE_string(
    "dir_obs_save",
    str(root.joinpath("datasets")),
    "the experimental",
)
flags.DEFINE_string(
    "author",
    "",
    "author tag for the dataset generation",
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
    ds_nadirs = load_xr_datasets_list(obs_files)

    for ifilename, ids in ds_nadirs.items():
        # save dataset
        ifilename = Path(FLAGS.dir_obs_save).joinpath(ifilename)
        logger.info(f"Saving NADIR, {ifilename}...")
        ids.to_netcdf(ifilename)

    logger.info("Get SWOT track files...")
    file_path = get_raw_altimetry_files(FLAGS.dir_obs, "swot")

    logger.info("Open KARIN SWOT dataset...")
    ds_karin_swot = xr.open_dataset(file_path[0])

    logger.info("Preprocess KARIN SWOT dataset...")
    ds_karin_swot = preprocess_karin_swot(ds_karin_swot, author=FLAGS.author)

    logger.debug("Checking size of swot data...")
    assert ds_karin_swot.coords["time"].shape == (8_412_216,)

    ifilename = Path(FLAGS.dir_obs_save).joinpath(file_path[0].name)
    logger.info(f"Saving KARIN SWOT, {ifilename}...")
    ds_karin_swot.to_netcdf(ifilename)

    # SWOT NADIR DATA
    logger.info("Get SWOT track files...")
    file_path = get_raw_altimetry_files(FLAGS.dir_obs, "swotnadir")

    logger.info("Open KARIN SWOT NADIR dataset...")
    ds_karin_swot_nadir = xr.open_dataset(file_path[0])

    # select the first cycle
    ds_karin_swot_nadir = ds_karin_swot_nadir.isel(cycle=0)

    logger.debug("Checking size of swot nadir data...")
    assert ds_karin_swot_nadir.coords["time"].shape == (161_333,)

    ifilename = Path(FLAGS.dir_obs_save).joinpath(file_path[0].name)
    logger.info(f"Saving KARIN SWOT NADIR, {ifilename}...")
    ds_karin_swot_nadir.to_netcdf(ifilename)

    logger.info(f"Done!")
    logger.debug(f"Time Taken: {time.time()-t0:.2f} secs")


if __name__ == "__main__":
    app.run(main)
