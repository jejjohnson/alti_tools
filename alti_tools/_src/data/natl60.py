from typing import List


OSSE_2020b_NATL0_ref = [
    "NATL60-CJM165_GULFSTREAM_y2013m09d30.1h_SSH.nc",
    "NATL60-CJM165_GULFSTREAM_y2013m09d29.1h_SSH.nc",

]

OSSE_2020b_NATL60_OBS_BASENAME = "2020a_SSH_mapping_NATL60"
OSSE_2020b_NATL60_REF_BASENAME = "NATL60-CJM165_GULFSTREAM"



def get_obs_name(dataset: str):
    """
    Datasets:
        * Jason
        * Envisat
        * Topex/Poseidon Interleaved
        * Geosat2
        * SWOT Nadir
        * Karin Nadir
    """

    # base name
    basename = OSSE_2020b_NATL60_OBS_BASENAME

    # mapping for correct name
    name_f = lambda file_name: basename + "_" + file_name


    if dataset == "jason1":
        return name_f("jason1.nc")
    elif dataset == "envisat":
        return name_f("envisat.nc")
    elif dataset == "tp":
        return name_f("topex-poseidon_interleaved.nc")
    elif dataset == "geosat2":
        return name_f("geosat2.nc")
    elif dataset == "nadir_swot":
        return name_f("nadir_swot.nc")
    elif dataset == "karin_swot":
        return name_f("karin_swot.nc")
    else:
        raise ValueError(f"Unrecognized dataset name '{dataset}'")


def get_obs_experiment(experiment: str="1nadir") -> List[str]:
    """
    Experiments:
        * '1nadir' - 1 NADIR track
        * '4nadir' - 4 NADIR tracks
        * '1swot' - 1 SWOT track
        * '1swot4nadir' - 1 SWOT, 4 NADIR
    """

    if experiment.lower() == "1nadir":
        return [
            get_obs_name("jason1"),
        ]

    elif experiment.lower() == "4nadir":
        return [
            get_obs_name("jason1"),
            get_obs_name("envisat"),
            get_obs_name("geosat2"),
            get_obs_name("tp")
        ]
    elif experiment.lower() == "1swot":
        return [
            get_obs_name("nadir_swot"),
            get_obs_name("karin_swot")
        ]
    elif experiment.lower() == "1swot4nadir":
        return [
            get_obs_name("nadir_swot"),
            get_obs_name("karin_swot"),
            get_obs_name("jason1"),
            get_obs_name("envisat"),
            get_obs_name("geosat2"),
            get_obs_name("tp")
        ]
    else:
        raise ValueError(f"Unrecognized experiment scenario: '{experiment}'.")