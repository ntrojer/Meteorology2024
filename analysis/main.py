import xarray as xr
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue
import cartopy.crs as ccrs
import core as core

import warnings
warnings.filterwarnings("ignore")

# location of era5 data on teachinghub
path="../../LEHRE/msc-intro-comp-met-ex-w2024/data/era5/"
#print(Path(path).resolve())

years= ["1950"]

"""# generate list of era5 files for a given year
def get_filelists(year: str):
    flist = list()
    for file in Path(path).rglob("era5-"+str(year)+"-01.nc"):
        flist.append(file)
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
"""
"""def multi_processing(years):
    filelists = []
    for year in years:
        filelists.append(get_filelists(year))
    for flist in filelists:
        #print(flist)
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
            #        # merge into yearly array
       # pvpot = np.stack(pvpot_chk, axis=0)
       # print(pvpot) 
"""

ds2=xr.open_mfdataset(path+"era5-1950-01.nc", chunks={"valid_time":1e5} )
ds2["wspd"] = core.windspeed(ds2)
pvpot2 = core.pv_pot(ds2).groupby(ds2.valid_time.dt.month).mean("valid_time").compute()
fig, ax = plt.subplots(figsize=(10, 8))

# Main plot: Contour plot of potential vorticity
contour = ax.contourf(ds2.longitude, ds2.latitude, pvpot2[0, :, :], cmap="viridis")
fig.colorbar(contour, ax=ax, orientation="vertical", label="Potential Vorticity")

# Inset plot: World map
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Define the inset position and dimensions (manually), then set projection
inset_position = [0.05, 0.05, 0.3, 0.3]  # [left, bottom, width, height] relative to the main plot
ax_inset = fig.add_axes(inset_position, projection=ccrs.PlateCarree())
ax_inset.set_global()
ax_inset.stock_img()  # Background world image
ax_inset.coastlines()
ax_inset.set_title("World Map", fontsize=8)

plt.show()
plt.savefig('pvpot.png')