import json
from alti_tools._src.utils.files import list_all_files


# GENERATE SCRIPT FOR OSSE NATL60 Data Challenge
directory = "/Volumes/EMANS_HDD/data/dc20a_osse/dc_obs"

json_file_list = dict()

# get obs files in directory
files = list_all_files(directory, full_path=False)
json_file_list["obs"] = files

# get reference files in directory
directory = "/Volumes/EMANS_HDD/data/dc20a_osse/dc_ref"
files = list_all_files(directory, full_path=False)
json_file_list["ref"] = files

# save to json
save_dir = "/Users/eman/code_projects/alti_tools/datasets/osse_2020a_natl60.json"

with open(save_dir, "w+") as f:
    json.dump(json_file_list, f)