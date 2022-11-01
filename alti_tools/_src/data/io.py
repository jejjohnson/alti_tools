import subprocess
import xarray as xr
from typing import List, Optional


# def load_data(path, data: str | List[str]):

#     if isinstance(data, "str"):
#         return xr.
        

#     return None

def runcmd(cmd, verbose = False, *args, **kwargs):
    """_summary_

    Args:
        cmd str: the command
        verbose (bool, optional): _description_. Defaults to False.

    Information:
    Command taken from:
        https://www.scrapingbee.com/blog/python-wget/
    """

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass


def get_aviso_session(username="str", password="str",):
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


