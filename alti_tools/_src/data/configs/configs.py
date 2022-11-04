from ml_collections import config_dict


def get_1nadir_config():
    config = config_dict.ConfigDict()

    config.file_names = [
        "2020a_SSH_mapping_NATL60_jason1.nc"
    ]

    return config


def get_reference_config():
    config = config_dict.ConfigDict()

    # SUBSET Arguments    
    config.preprocess = preprocess = config_dict.ConfigDict()
    # longitude subset
    preprocess.lon_min = 285.0
    preprocess.lon_max = 315.0
    preprocess.dlon = 0.2
    preprocess.lon_buffer = 1.0
    # latitude subset
    preprocess.lat_min = 23.0
    preprocess.lat_max = 53.0
    preprocess.dlat = 0.2
    preprocess.lat_buffer = 1.0
    # temporal subset
    preprocess.time_min = "2016-12-01"
    preprocess.time_max = "2018-01-31"
    preprocess.dtime = "1_D"
    preprocess.time_buffer = 7.0

    return config

def init_config(config=None):
    if config is None:
        config = config_dict.ConfigDict()
    return config

def get_osse_2020b_config():
    """The configuration parameters for the OSSE 2020 data challenge
    for the NATL60 SSH reconstruction from pseudo-observations
    """
    raise NotImplementedError()


def get_ose_2021b_aviso_data(username="str", password="str"):

    aviso = config_dict.ConfigDict()
    aviso.url_alongtrack = "https://tds.aviso.altimetry.fr/thredds/dodsC/2021a-SSH-mapping-OSE-along-track-data"
    aviso.url_map = "https://tds.aviso.altimetry.fr/thredds/dodsC/2021a-SSH-mapping-OSE-grid-data"

    return aviso


def get_ose_2021b_config(config=None):
    """The configuration parameters for the OSE 2021 data challenge
    for the SSH reconstruction from altimetry tracks
    """
    
    # initialize config
    config = init_config(config=config)

    # ====================
    # DATASET ARGS
    # ====================
    config.data = data = config_dict.DataDict()

    # Observation data
    data.obs_train_path = ""
    data.obs_train_files = [
        "dt_global_alg_phy_l3_20161201-20180131_285-315_23-53.nc",
        "dt_global_h2g_phy_l3_20161201-20180131_285-315_23-53.nc"
        "dt_global_j2g_phy_l3_20161201-20180131_285-315_23-53.nc"
        "dt_global_j2n_phy_l3_20161201-20180131_285-315_23-53.nc"
        "dt_global_j3_phy_l3_20161201-20180131_285-315_23-53.nc"
        "dt_global_s3a_phy_l3_20161201-20180131_285-315_23-53.nc"
    ]
    data.obs_eval_path = ""
    data.obs_eval_files = [
        "dt_global_c2_phy_l3_20161201-20180131_285-315_23-53.nc"
    ]
    data.ds_maps_base_path = ""
    data.ds_maps_files = [
        "OSE_ssh_mapping_BASELINE.nc"
        "OSE_ssh_mapping_BFN.nc"
        "OSE_ssh_mapping_DUACS.nc"
        "OSE_ssh_mapping_DYMOST.nc"
        "OSE_ssh_mapping_MIOST.nc"
        "OSE_ssh_mapping_4dvarNet.nc"
    ]
    data.ds_mdt_base_path = ""
    data.ds_mdt_files = [
        "mdt.nc"
    ]

    # ====================
    # INPUT DATA SUBSET
    # ====================
    config.preprocess = preprocess = config_dict.ConfigDict()
    # longitude subset
    preprocess.lon_min = 285.0
    preprocess.lon_max = 315.0
    preprocess.dlon = 0.2
    preprocess.lon_buffer = 1.0
    # latitude subset
    preprocess.lat_min = 23.0
    preprocess.lat_max = 53.0
    preprocess.dlat = 0.2
    preprocess.lat_buffer = 1.0
    # temporal subset
    preprocess.time_min = "2016-12-01"
    preprocess.time_max = "2018-01-31"
    preprocess.dtime = "1_D"
    preprocess.dtime_freq = 1
    preprocess.dtime_unit = "D"
    preprocess.time_buffer = 7.0

    # ==========================
    # EVALUATION DATA SUBSET
    # ==========================
    config.eval_data = eval_data = config_dict.ConfigDict()
    eval_data.lon_min = 295.0
    eval_data.lon_max = 305.0
    eval_data.dlon = 0.2
    eval_data.lat_min = 33.0
    eval_data.lat_max = 43.0
    eval_data.dlat = 0.2
    eval_data.time_min = "2017-01-01"
    eval_data.time_max = "2017-12-31"
    eval_data.dtime_freq = 1
    eval_data.dtime_unit = "D"
    eval_data.lon_buffer = 2.0
    eval_data.lat_buffer = 2.0
    eval_data.time_buffer = 7.0

    # =======================
    # PSD ARGUMENTS
    # =======================
    config.psd = psd = config_dict.ConfigDict()
    # binning along track
    psd.bin_lat_step = 1.0
    psd.bin_lon_step = 1.0
    psd.bin_time_step = "1D"
    psd.min_obs = 10
    # power spectrum
    psd.delta_t = 0.9434        # Cryosat-2 averaged delta-t in sample i s
    psd.velocity = 6.77         # Cryosat-2 ground velocity in km/s
    psd.delta_x = psd.velocity * psd.delta_t
    psd.length_scale = 1000     # segment length scale in km
    psd.jitter = 1e-4

    raise NotImplementedError()


def get_osse_2022b_config():
    """The configuration parameters for the OSSE 2022 data challenge
    for the Quasi-Geostrophic SSH from pseudo-observations
    """
    raise NotImplementedError()
