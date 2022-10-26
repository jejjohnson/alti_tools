import xarray as xr
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context(context="talk", font_scale=0.7)


def plot_psd_wavenumber(da: xr.DataArray):
    
    fig, ax = plt.subplots()

    ax.plot( 
        da.freq_r,
        da,
        label=getattr(da, "label", None)
    )

    ax.set(
        yscale="log", xscale="log",
        xlabel="Wavenumber [cycles/km]",
        ylabel="PSD [m$^{2}$/cycles/m]",
    )

    secax = ax.secondary_xaxis('top', functions=(lambda x: 1/(x+1e-20), lambda x: 1/(x+1e-20)))
    secax.xaxis.set_major_formatter('{x:.0f}')
    secax.set(xlabel="Wavelength [km]")


    ax.legend()
    ax.grid(which="both", alpha=0.5)
    
    return fig, ax


def plot_psd_wavelength(da: xr.DataArray):
    
    fig, ax = plt.subplots()

    ax.plot( 
        1/da.freq_r,
        da,
        label=getattr(da, "label", None)
    )

    ax.set(
        yscale="log", xscale="log",
        xlabel="Wavelength [km]",
        ylabel="PSD [m$^{2}$/cycles/m]",
    )

    ax.xaxis.set_major_formatter('{x:.0f}')
    ax.invert_xaxis()


    ax.legend()
    ax.grid(which="both", alpha=0.5)
    
    return fig, ax

def plot_psd(da: xr.DataArray):
    
    fig, ax = plt.subplots()

    ax.plot( 
        da.freq_r,
        da,
        label=getattr(da, "label", None)
    )


    ax.set(
        yscale="log", xscale="log",
        xlabel="Wavenumber [cycles/km]",
        ylabel="PSD [m$^{2}$/cycles/m]",
    )

    secax = ax.secondary_xaxis('top', functions=(lambda x: 1/(x+1e-20), lambda x: 1/(x+1e-20)))
    secax.xaxis.set_major_formatter('{x:.0f}')
    secax.set(xlabel="Wavelength [km]")


    ax.legend()
    ax.grid(which="both", alpha=0.5, color="gray")

    return fig, ax