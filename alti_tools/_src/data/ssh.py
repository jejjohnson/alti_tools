from .io import runcmd

BASE_URL = ""
URL_NATL60 = "https://ige-meom-opendap.univ-grenoble-alpes.fr//thredds/fileServer/meomopendap/extract/ocean-data-challenges/dc_data1/dc_ref/NATL60-CJM165_GULFSTREAM_y2013m09d30.1h_SSH.nc"
URL_4DVARNET = "https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/ocean-data-challenges/dc_data1/dc_mapping/2020a_SSH_mapping_NATL60_4DVarNet_v2022_nadirswot_GF_GF.nc"
URL_DUACS = "https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/ocean-data-challenges/dc_data1/dc_mapping/2020a_SSH_mapping_NATL60_DUACS_swot_en_j1_tpn_g2.nc"
URL_MIOST = "https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/ocean-data-challenges/dc_data1/dc_mapping/2020a_SSH_mapping_NATL60_MIOST_swot_en_j1_tpn_g2.nc"
URL_test = "https://raw.githubusercontent.com/adekunleoajayi/powerspec/master/powerspec/test/test_data.nc"

# OSSE OCEANIX DATASETS

URL_OSSE_OBS_BOTH_SSH = "https://s3.us-east-1.wasabisys.com/melody/osse_data/data/gridded_data_swot_wocorr/dataset_nadir_0d_swot.nc"
URL_OSSE_OBS_NADIR_SSH = "https://s3.us-east-1.wasabisys.com/melody/osse_data/data/gridded_data_swot_wocorr/dataset_nadir_0d.nc"
URL_OSSE_OBS_SWOT_SSH = "https://s3.us-east-1.wasabisys.com/melody/osse_data/data/gridded_data_swot_wocorr/dataset_swot.nc"
URL_OSSE_DUACS_SSH = (
    "https://s3.us-east-1.wasabisys.com/melody/osse_data/oi/ssh_NATL60_swot_4nadir.nc"
)
URL_OSSE_NATL60_SSH = "https://s3.us-east-1.wasabisys.com/melody/osse_data/ref/NATL60-CJM165_GULFSTREAM_ssh_y2013.1y.nc"
URL_OSSE_NATL60_SST = "https://s3.us-east-1.wasabisys.com/melody/osse_data/ref/NATL60-CJM165_GULFSTREAM_sst_y2013.1y.nc"
URL_OSSE_NATL60_SSC = "https://s3.us-east-1.wasabisys.com/melody/osse_data/ref/NATL60-CJM165_GULFSTREAM_sss_y2013.1y.nc"

# QG SIMULATIONS
URL_QG_IDEAL_SIMPLE_128 = "https://ige-meom-opendap.univ-grenoble-alpes.fr//thredds/fileServer/meomopendap/extract/dc2022b_q/qgsim_simple_128x128.nc"
URL_QG_IDEAL_FORCING_128 = "https://ige-meom-opendap.univ-grenoble-alpes.fr//thredds/fileServer/meomopendap/extract/dc2022b_q/qgsim_forcing_128x128.nc"
URL_QG_IDEAL_COMPLEX_128 = "https://ige-meom-opendap.univ-grenoble-alpes.fr//thredds/fileServer/meomopendap/extract/dc2022b_q/qgsim_complex_128x128.nc"
URL_QG_IDEAL_COMPLEX_256 = "https://ige-meom-opendap.univ-grenoble-alpes.fr//thredds/fileServer/meomopendap/extract/dc2022b_q/trial_res/qgsim_complex_256x256_L2_D2.nc"
URL_QG_IDEAL_COMPLEX_128 = "https://ige-meom-opendap.univ-grenoble-alpes.fr//thredds/fileServer/meomopendap/extract/dc2022b_q/trial_res/qgsim_complex_128x128_L1_D1.nc"
URL_QG_IDEAL_SIMPLE_128_1000s = "https://ige-meom-opendap.univ-grenoble-alpes.fr//thredds/fileServer/meomopendap/extract/dc2022b_q/qgsim_simple_128x128_dt1000.nc"

# QG SSH SIMULATIONS
URL_QG_SSH = "https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/ocean-data-challenges/2022b_SSH_QG_mapping/dc_qg_eval.tar.gz"


def get_ssh_url(dataset: str = "natl60") -> str:
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


def download_ssh_toy(dataset: str = "natl60", *args, **kwargs) -> None:
    url = get_ssh_url(dataset)
    runcmd(f"wget -nc {url}", *args, **kwargs)
    return None


def download_osse_demo(
    dataset: str = "",
    *args,
) -> None:

    return None
