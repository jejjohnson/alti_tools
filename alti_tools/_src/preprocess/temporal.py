import numpy as np
import xarray as xr


def rescale_temporal(ds, config):

    global_min = np.datetime64(config.time_min)
    dtime = np.timedelta64(config.time_delta)

    ds["time"] = (ds["time"].values - global_min) / dtime

    return ds


def subset_temporal(ds: xr.Dataset, config) -> xr.Dataset:

    time_min = np.datetime64(config.time_min)
    time_max = np.datetime64(config.time_max)

    ds = ds.sel(time=slice(time_min, time_max))
    # ds = ds.where((ds["time"] >= time_min) & (ds["time"] <= time_max))

    return ds
