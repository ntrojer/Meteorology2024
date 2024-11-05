import xarray as xr
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue

import core as core

import warnings
warnings.filterwarnings("ignore")

# location of era5 data on teachinghub
path="~/LEHRE/msc-intro-comp-met-ex-w2024/data/era5/"


# generate list of era5 files for a given year
def get_filelists(year: str):
    flist = list()
    #print(Path(path).rglob("era5-"+"1950"+"-*.nc"))
    print(list(Path(path).rglob("era5-"+"2000"+"-*.nc")))
    for file in Path(path).rglob("era5-"+year+"-*.nc"):
        flist.append(file)
        print(file)
    return flist

# function to compute time-mean pv potential, will be called by multiprocessing
def batchcompute_pvpot(file, queue):
    ds = xr.open_dataset(file, engine="netcdf4", chunks={"valid_time":1e5} )
    ds["wspd"] = core.windspeed(ds)
    pv_pot = core.pv_pot(ds).mean("valid_time").compute()
    queue.put(pv_pot)
    return None


nlat = 721;
nlon = 1440;

def multi_processing():
    years= ["1950","1951"]
    flist = []
    for year in years:
        flist.extend(get_filelists(year))
    print("flist", flist)
    # use 1 process per monthly file
    nprocs = len(flist)
    # output from each process
    pvpot_chk = np.zeros((nprocs,nlat,nlon))
    queue = Queue()
    processes = [Process(target=batchcompute_pvpot, 
                         args=(flist[i], queue)) for i in range(0, nprocs)]
    for process in processes: process.start() # start all processes
    for i in range(nprocs): # collect results from processes
        pvpot_chk[i] = queue.get()
    for process in processes: process.join()  # wait for all processes to complete
    # merge into yearly array
    #pvpot = np.stack(pvpot_chk, axis=0)

multi_processing()