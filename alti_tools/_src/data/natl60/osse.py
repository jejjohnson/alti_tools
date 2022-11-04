import json
import os
import warnings
from pathlib import Path
from typing import List

import numpy as np
import xarray as xr
from dask.array.core import PerformanceWarning

from alti_tools._src.data.configs.natl60 import get_osse_2020a_setup
from alti_tools._src.utils.files import (
    check_if_directory,
    check_if_file,
    check_list_equal_elem,
    get_subset_elements,
    list_all_files,
)
from alti_tools._src.utils.paths import get_root_path


def get_swot_obs_setup_files(files: List[str], setup: str = "nadir1"):

    # initialize setup config
    setup_config = get_osse_2020a_setup()

    # get specific scenario
    setup_filenames = setup_config[setup]

    setup_files = get_subset_elements(setup_filenames, files)

    assert len(setup_files) == len(setup_filenames)

    return setup_files


def get_obs_exp_files(obs_dir: str, experiment: str = "nadir1") -> List[str]:
    """
    Experiments:
    * "nadir1"
    * "nadir4"
    * "swot1"
    * "swot1nadir1"
    * "swot1nadir4"
    """

    data_config = get_osse_2020a_setup()

    obs_files = list(map(lambda x: Path(obs_dir).joinpath(x), data_config[experiment]))

    return obs_files


def check_osse_files(
    directory: str, json_file: dict = None, dataset: str = "obs"
) -> bool:

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
