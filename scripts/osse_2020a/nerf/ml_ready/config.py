from ml_collections import config_dict


def get_config():

    # initialize config dictionary
    config = config_dict.ConfigDict()

    ##########################
    # Spatial Temporal Subset
    ##########################

    # =======================
    # SPIN-UP REGION
    # =======================
    # training scenario
    config.subset = subset = config_dict.ConfigDict()
    # longitude bounds
    subset.lon_min = -65.0
    subset.lon_max = -55.0
    # latitude bounds
    subset.lat_min = 33.0
    subset.lat_max = 43.0
    # temporal bounds
    subset.time_min = "2012-10-01"  # we can start in the beginning of the nature run :)
    subset.time_max = "2012-12-02"

    return config
