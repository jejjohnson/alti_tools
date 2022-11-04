# Notebooks


## Data

---
### RAW

**`raw_natl60_swot_nadir.ipynb`**

> This notebook showcases how one can download the SWOT and NADIR data. It also has some light preprocessing steps necessary for the SWOT data to be more similar to the NADIR data. There is also some quick visualizations.

---
### Preprocess

**`osse_natl60_swot`**

> This notebook showcases how to


---
### Metrics

All of these notebooks are dealing with the power spectrum and the visualizations we can do.

* Isotropic Power Spectrum
* Spatial-Temporal Power Spectrum
* Power Spectrum Score

---
`alongtrack_psd.ipynb` [**TODO**]

> This notebook demonstrates how we can use the scipy signal processing to obtain a power spectrum of the along track.


---
`xrft_isotropic_walkthrough.ipynb`

> This notebook demonstrates how we can use the `xrft` package to calculate the isotropic power spectrum. It also includes a nice figure to visualize the wavenumber/wavelength versus the PSD with the proper units and scaling.


---
`spatiotemporal_powerspectrum.ipynb` [**TODO**]

> This notebook demonstrates how we can use the `xrft` package to calculate the spatial temporal power spectrum. 



---
`powerspectra_walkthrough.ipynb`

> This notebook demonstrates how to use the `powerspec` package to calculate the isotrophic power spectrum and then make nice plots of the wavelength/wavenumber versus PSD. 
> **Note**: This tutorial was included for legacy and verification reasons. I recommend using the `xrft` package instead as this is what is used within this package. See the above tutorial. 

