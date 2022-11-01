from ml_collections import config_dict


def get_data_config() -> config_dict.ConfigDict:
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
