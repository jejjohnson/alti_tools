import xarray as xr
import pandas as pd
from ..utils.tracking import get_current_timestamp


def preprocess_karin_swot(ds: xr.Dataset, author: str = ""):

    # reset coordinates
    # ds = ds.reset_coords(["nC"])

    # flatten dataset [NC, Time] -> [NC x Time]
    ds = ds.stack(z=("nC", "time")).dropna(dim="z").reset_index("time")

    # rename coordinate
    ds = ds.swap_dims({"z": "time"})

    # reset coordinates
    ds = ds.reset_coords(["z"])

    # sort by time
    ds = ds.sortby("time")

    # convert time to pandas
    ds["time"] = pd.to_datetime(ds["time"])

    # modify attributes (author, datetime processing)
    ds.attrs["mods_author"] = author
    ds.attrs["mods_time"] = get_current_timestamp()
    ds.attrs[
        "mods_desc"
    ] = f"Alongtrack conversion: Flattened Array, Swapped dimensions, Sorted wrt time, pandas datetime"

    return ds
