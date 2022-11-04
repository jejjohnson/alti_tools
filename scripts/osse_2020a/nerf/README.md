# NerF Project Preprocessing


**Downloading**

```bash
bash scripts/osse_2020a/data/dc20a_osse.sh /Volumes/EMANS_HDD/data/dc20a_osse/test/raw
```

**Preprocessing**

```bash
bash scripts/osse_2020a/nerf/preprocess/run.sh /Volumes/EMANS_HDD/data/dc20a_osse/test/raw/dc_obs /Volumes/EMANS_HDD/data/dc20a_osse/test/preprocess/osse_2020a_natl60
```

**ML Ready Preprocessing**

```bash
bash scripts/osse_2020a/nerf/ml_ready/run.sh /Volumes/EMANS_HDD/data/dc20a_osse/test/preprocess/ /Volumes/EMANS_HDD/data/dc20a_osse/test/ml
```

