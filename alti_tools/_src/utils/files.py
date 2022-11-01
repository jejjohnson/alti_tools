from typing import List 
from pathlib import Path

def check_if_directory(directory: str):

    if not Path(directory).exists():
        raise ValueError("Directory doesn't exist...")
    else:
        return True


def check_if_file(directory: str):

    if not Path(directory).is_file():
        raise ValueError("File doesn't exist...")
    else:
        return True


def list_all_files(directory: str, ext: str="**/*", full_path: bool=True)-> List[str]:

    # check if directory exists
    check_if_directory(directory)

    files = [x for x in Path(directory).glob(ext) if x.is_file()]

    if not full_path:
        files = get_file_names(files)
    
    return files


def get_file_names(files: List[str]):

    # convert to Path file
    files = list(map(lambda x: Path(x), files))

    # get file names
    files = list(map(lambda x: x.name, files)) 

    return files


def check_list_equal_elem(list1: List[str], list2: List[str]):

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False