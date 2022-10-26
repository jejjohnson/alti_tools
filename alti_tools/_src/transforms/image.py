from typing import Optional, Union

import numpy as np
import pnadas as pd
from einops import rearrange


def get_image_coordinates(image, min_val: int=-1, max_val: int=1):
    # get image size
    image_height, image_width, _ = image.shape

    # get all coordinates
    coordinates = [
        np.linspace(min_val, max_val, num=image_height),
        np.linspace(min_val, max_val, num=image_width)
    ]

    # create meshgrid of pairwise coordinates
    coordinates = np.meshgrid(*coordinates, indexing="ij")

    # stack tensors together
    coordinates = np.stack(coordinates, axis=-1)

    # rearrange to coordinate vector
    coordinates = rearrange(coordinates, "h w c -> (h w) c")
    pixel_values = rearrange(image, "h w c -> (h w) c")

    return coordinates, pixel_values



def minmax_scaler(x: np.ndarray, min_val: Optional[Union[np.ndarray, float]], max_val) -> float:
    return (x - min_val) / (max_val - min_val)


def minmax_unscaler(x: np.ndarray, min_val: Optional[Union[np.ndarray, float]], max_val) -> float:
    return x * (max_val - min_val) + min_val

