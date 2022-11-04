from dataclasses import dataclass

import numpy as np
from numpy import datetime64
import xarray as xr


from alti_tools._src.transforms.spatial import convert_lon_360_180


@dataclass
class SpatialTemporalBounds:
    lon_min: float
    lon_max: float
    dlon: float
    lat_min: float
    lat_max: float
    dlat: float
    time_min: np.datetime64
    time_max: np.datetime64
    dtime: np.datetime64

    def grid_lon(self):
        return np.arange(self.lon_min, self.lon_max + self.dlon, self.dlon)

    def grid_lat(self):
        return np.arange(self.lat_min, self.lat_max + self.dlat, self.dlat)

    def grid_time(self):
        return np.arange(self.time_min, self.time_max + self.dtime, self.dtime)


def create_spatialtemporal_grid(
    lon_min, lon_max, dlon, lat_min, lat_max, dlat, time_min, time_max, dtime
):

    grid_lon = np.arange(lon_min, lon_max + dlon, dlon)
    grid_lat = np.arange(lat_min, lat_max + dlat, dlat)
    grid_time = np.arange(time_min, time_max + dtime, dtime)

    return grid_lon, grid_lat, grid_time


def rescale_spatial(ds: xr.Dataset, config) -> xr.Dataset:

    # longitude
    global_min = config.lon_min
    dlon = config.lon_delta

    ds["lon"] = (ds["lon"].values - global_min) / dlon

    # latitude
    global_min = config.lat_min
    dlat = config.lat_delta

    ds["lat"] = (ds["lat"].values - global_min) / dlat

    return ds


def correct_longitude(ds, angle: str = "180"):

    # lon_min = ds.lon.min().values

    # if lon_min < 0:
    #     ds['lon'] = xr.where(ds['lon'] >= 180., ds['lon']-360., ds['lon'])
    if angle == "180":
        ds["lon"] = convert_lon_360_180(ds["lon"])
    else:
        ds["lon"] = xr.where(ds["lon"] >= 180.0, ds["lon"] - 360.0, ds["lon"])

    return ds


def subset_spatial(ds, config):

    ds = ds.where(
        (ds["lon"] >= config.lon_min)
        & (ds["lon"] <= config.lon_max)
        & (ds["lat"] >= config.lat_min)
        & (ds["lat"] <= config.lat_max),
        drop=True,
    )

    return ds
