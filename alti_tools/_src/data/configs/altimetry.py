from ml_collections import config_dict
from pathlib import Path
from typing import List


def get_raw_altimetry_files(obs_dir: str=None, dataset: str="nadir") -> List[str]:
    """
    Experiments:
    * "nadir"
    * "swot"
    * "swotnadir"
    """

    data_config = get_raw_altimetry_config()

    if obs_dir is None:
        obs_dir = ""
    
    obs_files = list(map(lambda x: Path(obs_dir).joinpath(x), data_config[dataset]))

    return obs_files

def get_raw_altimetry_config() -> config_dict.ConfigDict:
    config = config_dict.ConfigDict()

    # SUBSET Arguments    
    config.nadir = [
        "2020a_SSH_mapping_NATL60_topex-poseidon_interleaved.nc",
        "2020a_SSH_mapping_NATL60_envisat.nc",
        "2020a_SSH_mapping_NATL60_geosat2.nc",
        "2020a_SSH_mapping_NATL60_jason1.nc"
    ]

    config.swot = [
        "2020a_SSH_mapping_NATL60_karin_swot.nc",
    ]
    config.swotnadir = [        
        "2020a_SSH_mapping_NATL60_nadir_swot.nc",
    ]


    return config


def get_osse_2020a_data_config() -> config_dict.ConfigDict:
    config = config_dict.ConfigDict()

    # SUBSET Arguments    
    config.nadir4 = [
        "2020a_SSH_mapping_NATL60_topex-poseidon_interleaved.nc",
        "2020a_SSH_mapping_NATL60_envisat.nc",
        "2020a_SSH_mapping_NATL60_geosat2.nc",
        "2020a_SSH_mapping_NATL60_jason1.nc"
    ]

    config.nadir1 = [
        "2020a_SSH_mapping_NATL60_jason1.nc"
    ]

    config.swot1 = [
        "2020a_SSH_mapping_NATL60_karin_swot.nc",
        "2020a_SSH_mapping_NATL60_nadir_swot.nc"
    ]
    config.swot1nadir1 = [        
        "2020a_SSH_mapping_NATL60_karin_swot.nc",
        "2020a_SSH_mapping_NATL60_nadir_swot.nc",
        "2020a_SSH_mapping_NATL60_jason1.nc"
    ]
    config.swot1nadir4 = [        
        "2020a_SSH_mapping_NATL60_karin_swot.nc",
        "2020a_SSH_mapping_NATL60_nadir_swot.nc",
        "2020a_SSH_mapping_NATL60_topex-poseidon_interleaved.nc",
        "2020a_SSH_mapping_NATL60_envisat.nc",
        "2020a_SSH_mapping_NATL60_geosat2.nc",
        "2020a_SSH_mapping_NATL60_jason1.nc"
    ]


    return config