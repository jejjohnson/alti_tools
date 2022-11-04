from ml_collections import config_dict


def get_osse_2020a_setup() -> config_dict.ConfigDict:
    config = config_dict.ConfigDict()

    # SUBSET Arguments
    config.nadir4 = [
        "2020a_SSH_mapping_NATL60_topex-poseidon_interleaved.nc",
        "2020a_SSH_mapping_NATL60_envisat.nc",
        "2020a_SSH_mapping_NATL60_geosat2.nc",
        "2020a_SSH_mapping_NATL60_jason1.nc",
    ]

    config.nadir1 = ["2020a_SSH_mapping_NATL60_jason1.nc"]

    config.swot1 = [
        "2020a_SSH_mapping_NATL60_karin_swot.nc",
        "2020a_SSH_mapping_NATL60_nadir_swot.nc",
    ]
    config.swot1nadir1 = [
        "2020a_SSH_mapping_NATL60_karin_swot.nc",
        "2020a_SSH_mapping_NATL60_nadir_swot.nc",
    ]
    config.swot1nadir4 = [
        "2020a_SSH_mapping_NATL60_karin_swot.nc",
        "2020a_SSH_mapping_NATL60_nadir_swot.nc",
        "2020a_SSH_mapping_NATL60_topex-poseidon_interleaved.nc",
        "2020a_SSH_mapping_NATL60_envisat.nc",
        "2020a_SSH_mapping_NATL60_geosat2.nc",
        "2020a_SSH_mapping_NATL60_jason1.nc",
    ]

    return config


def get_osse_2020a_preprocess():

    # initialize config dictionary
    config = config_dict.ConfigDict()

    # training scenario
    config.data = data = config_dict.ConfigDict()
    data = "swothnadir4"  # "nadir1", "nadir4", "swot", "swothnadir4"

    ##########################
    # Spatial Temporal Subset
    ##########################
    config.subset = subset = config_dict.ConfigDict()

    # =======================
    # SPIN-UP REGION
    # =======================
    # training scenario
    config.subset.spinup = spinup = config_dict.ConfigDict()
    # longitude bounds
    spinup.lon_min = -65.0
    spinup.lon_max = -55.0
    # latitude bounds
    spinup.lat_min = 33.0
    spinup.lat_max = 43.0
    # temporal bounds
    spinup.time_min = "2012-10-01"  # we can start in the beginning of the nature run :)
    spinup.time_max = "2012-10-22"

    # =======================
    # TRAINING REGION
    # =======================
    # training scenario
    config.subset.train = train = config_dict.ConfigDict()
    train.spinup = True  # option to include spin in training
    # longitude bounds
    train.lon_min = -65.0
    train.lon_max = -55.0
    # latitude bounds
    train.lat_min = 33.0
    train.lat_max = 43.0
    # temporal bounds
    train.time_min = "2013-01-02"  # we can start in the beginning of the nature run :)
    train.time_max = "2013-09-30"

    # =======================
    # TEST REGION
    # =======================
    # training scenario
    config.subset.evaluation = evaluation = config_dict.ConfigDict()
    # longitude bounds
    evaluation.lon_min = -65.0
    evaluation.lon_max = -55.0
    # latitude bounds
    evaluation.lat_min = 33.0
    evaluation.lat_max = 43.0
    # temporal bounds
    evaluation.time_min = (
        "2012-10-22"  # we can start in the beginning of the nature run :)
    )
    evaluation.time_max = "2012-12-02"

    return config
