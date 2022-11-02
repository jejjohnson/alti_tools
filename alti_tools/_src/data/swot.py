import xarray as xr
from typing import List
from dask.array.core import PerformanceWarning
import warnings
from pathlib import Path


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


def load_xr_datasets_list(files: List[str]):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=PerformanceWarning)
        # Note: there is an annoying performance memory due to the chunking
        ds = dict()

        for ifile in files:
            ds[str(Path(ifile).name)] = xr.open_dataset(ifile)

    return ds
