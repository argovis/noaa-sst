This repo contains scripts and data for populating NOAA SST information from https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.html in Argovis.

## Rebuilding from scratch

 - Make sure you've created empty collections for NOAA SST data in MongoDB via the `sst-noaa-ol.py` script in [https://github.com/argovis/db-schema](https://github.com/argovis/db-schema).
 - Build the image described in `Dockerfile` as `argovis/noaa-sst:dev`; run a pod per `pod.yaml` or equivalent container based on it in the appropriate kube namespace or docker container network to connect to your MongoDB container, and the default Dockerfile CMD should run `run.sh` to fetch the data and populate the collections.
 - Build and run the image described in `Dockerfile-summary` to update summary docs (todo: could fold this into the previous step on the next major development cycle)
 - The proofreading items contain a simple random pythonic doublecheck.
