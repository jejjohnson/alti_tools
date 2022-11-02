import os
from pathlib import Path
import json
import xarray as xr
import numpy as np
from ..utils.files import check_if_directory, list_all_files, check_if_file, check_list_equal_elem
from ..utils.paths import get_root_path
import warnings
from typing import List
from dask.array.core import PerformanceWarning

from alti_tools._src.data.configs.natl60 import get_data_config

def get_obs_exp_files(obs_dir: str, experiment: str="nadir1") -> List[str]:
    """
    Experiments:
    * "nadir1"
    * "nadir4"
    * "swot1"
    * "swot1nadir1"
    * "swot1nadir4"
    """

    data_config = get_data_config()
    
    obs_files = list(map(lambda x: Path(obs_dir).joinpath(x), data_config[experiment]))

    return obs_files




def load_eval_ds(path: str):
    # load ref data
    ds = xr.open_mfdataset(path+"*.nc", combine="nested", concat_dim="time", parallel=True)

    # expected size (time,lat,lon)=(8760,600,600)
    # domain analysis
    time_min, time_max = np.datetime64("2012-10-22"), np.datetime64("2012-12-02")
    lon_min, lon_max = -64.975, 55.007
    lat_min, lat_max = 33.025, 42.9917

    # subset
    ds = ds_ref.sel(
        time=slice(time_min, time_max),
        lon=slice(lon_min, lon_max),
        lat=slice(lat_min, lat_max),
        drop=True,
    ).resample(time="1D").mean()

    # expected size (time,lat,lon)=(42,598,598)

    return None


def prepare_ds(ds):

    # rename variables
    ds = ds.rename({"ssh": "gssh"})

    # rescale time
    ds["time"] = ds["time"] - np.timedelta64(12, "h")

    return ds


def check_osse_files(directory: str, json_file: dict=None, dataset: str="obs") -> bool:

    if json_file is None:
        json_file = get_root_path().joinpath("datasets/osse_2020a_natl60.json")

    check_if_file(json_file)

    # load json directory
    with open(json_file, "r") as f: 
        json_file_list = json.load(f)

    # get files in directory
    obs_files = list_all_files(directory, ext="*.nc", full_path=False)

    # check if files are the same
    check_list_equal_elem(obs_files, json_file_list[dataset])

    
    return None

# def check_ref_data(path: str):

#     # get list of all files in folder

#     # check if list of files in folder is the same

#     # return false if not



