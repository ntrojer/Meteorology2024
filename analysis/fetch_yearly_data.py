import xarray as xr
import numpy as np
from pathlib import Path
from multiprocessing import Process, Queue
import argparse
import warnings
import core as core

path="../../LEHRE/msc-intro-comp-met-ex-w2024/data/era5/"
def get_filelists(years,new_data):
    if new_data:
        for year in years:
            ds2=xr.open_mfdataset(path+"era5-"+year+"-*.nc", chunks={"valid_time":1e5} )
            ds2["wspd"] = core.windspeed(ds2)
            ds2["pvpot2"] = core.pv_pot(ds2).groupby(ds2.valid_time.dt.month).mean("valid_time").compute()
            # pvpot2 = core.pv_pot(ds2).groupby(ds2.valid_time.dt.month).mean("valid_time").compute()
            ds2[["pvpot2", "longitude", "latitude"]].to_netcdf("era5-"+year+".nc")
    else:
        ds2 = xr.open_dataset("complete_data.nc")
    return ds2