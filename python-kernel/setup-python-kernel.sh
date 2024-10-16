# note: 
# 1. cdsapi requires cgi, which was removed from python in python3.11; I am therefore specifying a lower python version
# 2. I also found that I need to use numpy1 and not the new numpy2, which came out in summer 2024

# move to SRV home directory
cd /srvfs/home/avoigt

KNAME="intro-comp-meteo-ex-w2024"  # name of python kernel
ROOTPREFIX="/srvfs/home/avoigt/micromamba"

module load micromamba
micromamba create -n $KNAME -r $ROOTPREFIX
micromamba install -c conda-forge -n $KNAME -r $ROOTPREFIX python=3.10 \ pandas \ numpy=1.26.4 \ matplotlib \ cartopy \ netcdf4 \ xarray \ dask \ zarr \ cdsapi \ ipykernel

# create Jupyter kernel and make available
${ROOTPREFIX}/envs/${KNAME}/bin/python3 -m ipykernel install --user --name=$KNAME

# export environment setup to env.txt
micromamba env export -p ${ROOTPREFIX}/envs/${KNAME}/ > env.txt

