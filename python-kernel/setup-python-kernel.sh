# move to SRV home directory
cd /srvfs/home/avoigt

KNAME="intro-comp-meteo-ex-w2024"  # name of pyhton kernel
ROOTPREFIX="/srvfs/home/avoigt/micromamba"

module load micromamba
micromamba create -n $KNAME -r $ROOTPREFIX
micromamba install -c conda-forge -n $KNAME -r $ROOTPREFIX xarray \ pandas \ numpy \ matplotlib \ cartopy \ netcdf4
micromamba install -c conda-forge -n $KNAME -r $ROOTPREFIX dask \ zarr 
micromamba install -c conda-forge -n $KNAME -r $ROOTPREFIX cdsapi

# create Jupyter kernel and make available
micromamba install -c conda-forge -n $KNAME -r $ROOTPREFIX ipykernel
${ROOTPREFIX}/envs/${KNAME}/bin/python3 -m ipykernel install --user --name=$KNAME

# export evironment setup to env.txt
micromamba env export -p ${ROOTPREFIX}/envs/${KNAME}/ > env.txt

