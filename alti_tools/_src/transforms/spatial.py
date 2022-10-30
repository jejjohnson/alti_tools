import numpy as np

def spherical_to_cartesian_3d(lon, lat, radius: float=6371.010):
    
    x = radius * np.cos(lat) * np.cos(lon)
    y = radius * np.cos(lat) * np.sin(lon)
    z = radius * np.sin(lat)
    
    return x, y, z


def cartesian_to_spherical_3d(x, y, z):
    
    radius = np.sqrt(x**2 + y**2 + z**2)
    lon = np.arctan2(y, x)
    lat = np.arcsin( z / radius)
    
    return lon, lat, radius

def correct_coordinate_labels(ds):
    try:
        ds = ds.rename({"lat": "latitude"})
    except ValueError:
        pass

    try:
        ds = ds.rename({"lon": "longitude"})
    except ValueError as e:
        pass

    return ds



def coords_degree_2_meters(ds):
    """TODO: Adhoc
    User proper coordinate transformation
    """
    
    try:
        ds = ds.assign_coords(coords={"lat": ds["lat"] * 111e3})
        ds.lat.attrs["units"] = "m"
    except:
        pass
    
    try:
        ds = ds.assign_coords(coords={"lon": ds["lon"] * 111e3})
        ds.lon.attrs["units"] = "m"
    except:
        pass
    
    return ds


def coords_meters_2_degrees(ds):
    
    raise NotImplementedError()
    
    
def coords_rescale_meters(ds):
    
    raise NotImplementedError()
    
    