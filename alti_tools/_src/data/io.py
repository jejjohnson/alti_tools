import subprocess
import warnings
from pathlib import Path
from typing import List, Optional

import xarray as xr
from dask.array.core import PerformanceWarning

# def load_data(path, data: str | List[str]):

#     if isinstance(data, "str"):
#         return xr.


#     return None


def runcmd(cmd, verbose=False, *args, **kwargs):
    """_summary_

    Args:
        cmd str: the command
        verbose (bool, optional): _description_. Defaults to False.

    Information:
    Command taken from:
        https://www.scrapingbee.com/blog/python-wget/
    """

    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass


def get_aviso_session(
    username="str",
    password="str",
):
    try:
        import requests as rq
    except:
        raise ValueError("The requests package is not installed. Cannot use aviso.")

    aviso_session = rq.get_session()
    aviso_session.auth = (username, password)

    return aviso_session


def load_aviso_alongtrack(url: str, session: str):

    ds_store_url = xr.backendsPydapDataStore.open(url, session=session)

    return xr.open_dataset(ds_store_url)


def load_xr_datasets_list(files: List[str]):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=PerformanceWarning)
        # Note: there is an annoying performance memory due to the chunking
        ds = dict()

        for ifile in files:
            ds[str(Path(ifile).name)] = xr.open_dataset(ifile)

    return ds


def load_alongtrack_parallel(files: List[str], preprocess=None) -> xr.Dataset:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=PerformanceWarning)
        # Note: there is an annoying performance memory due to the chunking

        ds = xr.open_mfdataset(
            files,
            combine="nested",
            concat_dim="time",
            parallel=True,
            preprocess=preprocess,
            engine="netcdf4",
        )
        ds = ds.sortby("time")

    return ds
