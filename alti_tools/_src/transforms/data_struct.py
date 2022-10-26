from typing import List
import pandas as pd
import numpy as np


def array_2_df(coords, data, names: List[str]=["data"]):

    data = np.hstack([coords, data])
    
    if isinstance(names, str):
        names = [names]
    
    assert len(names) == data.shape[1]

    if coords.shape[1] == 1:
        columns = ["Nx"]
    elif coords.shape[1] == 2:
        columns = ["Nx", "Ny"]
    else:
        columns = ["Nx", "Ny", "Nt"]

    return pd.DataFrame(data, columns=columns).set_index(columns)



def array_2_xr(coords, data, names: List[str]=["data"]):
    return array_2_df(coords, data, names).to_xarray()


