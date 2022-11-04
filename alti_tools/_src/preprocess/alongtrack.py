import xarray as xr


def coarsen_alongtrack(ds: xr.Dataset, config) -> xr.Dataset:

    boundary = config.get("boundary", "trim")
    coarsen = config.get("time_steps", 5)
    summary = config.get("summary", "mean")

    if summary == "median":
        ds = ds.coarsen({"time": coarsen}, boundary=boundary).median()
    else:
        ds = ds.coarsen({"time": coarsen}, boundary=boundary).mean()

    return ds
