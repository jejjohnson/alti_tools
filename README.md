# Ocean Simulation Data Tools


A collection of useful tools for downloading, preprocessing and postprocessing ocean data (e.g. sea surface height, sea surface temperature, u, v, etc).

> Note: Most of the stuff in here is syntactic sugar but it helps to demonstrate how this would work in practice.


---
## Datasets

* 1 Layer Quasi-Geostrophic Simulations with NADIR-like and SWOT-like pseudo-observations
* NATL60 Simulations with NADIR and SWOT pseudo-observations over the Gulfstream, 1 year
* Altimetry Data over the Gulfstream, 1 year
* Global Altimetry data for 5 years
* Ensembles MEDWEST60 Simulations over the Mediterranean for 3 months.


---
### Dataset Structure

**WARNING**: Once we download the data to a raw folder, we never touch it again.

```
raw (DOWNLOAD ONLY)
│   reference
│   observations
experiment
└───preprocess
│    │  reference
│    │  observations
└───model
│    │  train    
│    │  test
│    │  eval
└───results
│    │  trial1    
│    │  trial2
│    │  trial3
└───analysis
│    │  maps
│    │  stats    
└───viz
     │  data
     │  maps
     │  stats   
```


---
## Recipes

The basis of this repo is to build consistent, replicable recipes that people can follow to go from the raw data to the results and everything in between.

Some key recipes will include:
* `Raw`: Downloading the raw data from a server to your local/cloud machine.
* `Preprocess`: Preprocessing the raw data to something more manageable (e.g cleaning, reformatting, etc)
* `Model Ready`: Do some additional transformations to make the data ready for ML (e.g. scaling, chunking)
* `Model Results`: Downloading some results from the models in a readable format.
* `PostProcess`: Post-processing and analysis of the results data to be ready for visualization
* `Viz`: Tools and scripts to generate nice plots for the metrics (e.g. PSD, interactive plots, GIFs)


---
## Functionality


Some example functionalities:

* Downloading Data
* Preprocessing Data (reformat, light cleaning, spatio-temporal subsets)
* Generating metrics