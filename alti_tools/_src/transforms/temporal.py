import numpy as np
import pandas as pd
import xarray as xr


def julian_data_transform(x: str):
    return pd.DatatimeIndex(x).to_julian_date().values


def coords_temporal_normalize(ds: xr.Dataset, factor: np.timedelta64=None) -> xr.Dataset:
    
    if factor is None:
        factor = np.timedelta64(1, "D")
        
    ds["time"] = (ds.time - ds.time[0]) / factor
    
    return ds