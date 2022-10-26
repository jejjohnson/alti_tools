import numpy as np
from dataclasses import dataclass
from numpy import datetime64


@dataclass
class SpatialTemporalBounds:
    lon_min: float
    lon_max: float
    dlon: float
    lat_min: float
    lat_max: float
    dlat: float
    time_min: np.datetime64
    time_max: np.datetime64
    dtime: np.datetime64

    def grid_lon(self):
        return np.arange(self.lon_min, self.lon_max + self.dlon, self.dlon)

    def grid_lat(self):
        return np.arange(self.lat_min, self.lat_max + self.dlat, self.dlat)

    def grid_time(self):
        return np.arange(self.time_min, self.time_max + self.dtime, self.dtime)

    


def create_spatialtemporal_grid(lon_min, lon_max, dlon, lat_min, lat_max, dlat, time_min, time_max, dtime):

    grid_lon = np.arange(lon_min, lon_max + dlon, dlon)
    grid_lat = np.arange(lat_min, lat_max + dlat, dlat)
    grid_time = np.arange(time_min, time_max + dtime, dtime)

    return grid_lon, grid_lat, grid_time