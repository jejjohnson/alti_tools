from .io import runcmd

BASE_URL = ""
URL_NATL60 = "https://ige-meom-opendap.univ-grenoble-alpes.fr//thredds/fileServer/meomopendap/extract/ocean-data-challenges/dc_data1/dc_ref/NATL60-CJM165_GULFSTREAM_y2013m09d30.1h_SSH.nc"
URL_4DVARNET = "https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/ocean-data-challenges/dc_data1/dc_mapping/2020a_SSH_mapping_NATL60_4DVarNet_v2022_nadirswot_GF_GF.nc"
URL_DUACS = "https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/ocean-data-challenges/dc_data1/dc_mapping/2020a_SSH_mapping_NATL60_DUACS_swot_en_j1_tpn_g2.nc"
URL_MIOST = "https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/ocean-data-challenges/dc_data1/dc_mapping/2020a_SSH_mapping_NATL60_MIOST_swot_en_j1_tpn_g2.nc"
URL_test = "https://raw.githubusercontent.com/adekunleoajayi/powerspec/master/powerspec/test/test_data.nc"

def get_ssh_url(dataset: str="natl60")->str:
    if dataset.lower() == "natl60":
        return URL_NATL60
    elif dataset.lower() == "4dvarnet":
        return URL_4DVARNET
    elif dataset.lower() == "duacs":
        return URL_DUACS
    elif dataset.lower() == "miost":
        return URL_MIOST
    elif dataset.lower() == "test":
        return URL_test
    else:
        raise ValueError("Unrecognized dataset")


def download_ssh_toy(dataset: str="natl60", *args, **kwargs) -> None:    
    url = get_ssh_url(dataset)
    runcmd(f"wget -N {url}",  *args, **kwargs)
    return None
