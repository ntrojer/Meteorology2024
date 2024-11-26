import xarray as xr
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue
import cartopy.crs as ccrs
import core as core
import cartopy.feature as cfeature
import argparse
import warnings
import fetch_monthly_data
import fetch_yearly_data

warnings.filterwarnings("ignore")

# location of era5 data on teachinghub
path="../../LEHRE/msc-intro-comp-met-ex-w2024/data/era5/"

parser = argparse.ArgumentParser()
parser.add_argument("--new_data", action="store_true", help="If you want to save time fetching the data, set this to false")
args = parser.parse_args()

# TODO: change these two lines in arguments that allows you to set the date range
monthly = True # change this to False if you want yearly data
years= ["1950"]


if monthly:
    ds2 = fetch_monthly_data.fetch_monthly_data(path=path, new_data=args.new_data)
    Path("monthly_plots").mkdir(parents=True, exist_ok=True)
else:
    # uncomment this if you want to fetch monthly data
    ds2=fetch_yearly_data.get_filelists(years,new_data=args.new_data)
    Path("yearly_plots").mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': ccrs.PlateCarree()})

# Main plot: Contour plot of potential vorticity
contour = ax.contourf(ds2.longitude, ds2.latitude, ds2.pvpot2[0, :, :], cmap="viridis")
fig.colorbar(contour, ax=ax, orientation="vertical", label="Potential Vorticity")

ax.coastlines(color='white', linewidth=0.7)
ax.add_feature(cfeature.BORDERS, edgecolor='white', linewidth=0.5)

gl = ax.gridlines(draw_labels=True, linestyle="None")
gl.top_labels = False  # Disable top labels
gl.right_labels = False  # Disable right labels
gl.xlabel_style = {'size': 10, 'color': 'black'}
gl.ylabel_style = {'size': 10, 'color': 'black'}

plt.show()
if monthly: 
    plt.savefig('monthly_plots/pvpot-1950-01.png')
else:
    plt.savefig('monthly_plots/pvpot-1950.png')