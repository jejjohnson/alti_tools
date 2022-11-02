import xarray as xr
from alti_tools._src.utils.tracking import get_current_timestamp


def preprocess_karin_swot(file_path: str, author: str=""):

    # open stacked dataset
    ds = xr.open_dataset(file_path)

    # flatten dataset [NC, Time] -> [NC x Time]
    ds = ds.stack(z=("nC", "time")).dropna(dim="z").reset_index("time")

    # rename coordinate
    ds = ds.swap_dims({"z": "time"})

    # sort by time
    ds = ds.sortby("time")

    # convert time to pandas
    ds["time"] = pd.to_datetime(ds["time"])

    # modify attributes (author, datetime processing)
    mods = dict()
    mods["author"] = author
    mods["time"] = get_current_timestamp()
    mods[""]
    ds.attrs["mods"] = mods
    
    return ds