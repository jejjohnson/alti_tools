import numpy as np
import pandas as pd
import xarray as xr

from dataclasses import dataclass
import datetime


def julian_data_transform(x: str):
    return pd.DatatimeIndex(x).to_julian_date().values


def coords_temporal_normalize(ds: xr.Dataset, factor: np.timedelta64=None) -> xr.Dataset:
    
    if factor is None:
        factor = np.timedelta64(1, "D")
        
    ds["time"] = (ds.time - ds.time[0]) / factor
    
    return ds


@dataclass
class TimeCentralCoords:
    central_date: datetime.datetime
    delta_t: datetime.datetime

    def __init__(self, central_date, delta_t):
        self.tmin = central_date - delta_t
        self.tmax = central_date + delta_t
        return None

@dataclass
class TimeBoundCoords:
    min_time: datetime
    max_time: datetime
    delta_t: datetime
    buffer_t: datetime
