import xrft
from dask.diagnostics import ProgressBar


def isotropic_power_spectrum(ds, **kwargs):
    # TODO: get config file

    # compute power spectrum (window=True
    signal_psd = xrft.isotropic_power_spectrum(
        ds, dim=['lat','lon'], 
        detrend='linear', window="tukey", 
        nfactor=2,
        window_correction=True, true_amplitude=True, truncate=True
    )

    # calculate mean signal
    signal_psd_mean = signal_psd.mean(dim=['time'], skipna=True)
    
    return signal_psd_mean

def isotropic_power_spectrum_dask(ds):
    
    with ProgressBar():
        signal = ds.chunk({"time":1, 'lon': ds['lon'].size, 'lat': ds['lat'].size})
        
        signal_psd_mean = isotropic_power_spectrum(signal)
        
    return signal_psd_mean