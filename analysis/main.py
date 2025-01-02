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
#import fetch_monthly_data
import fetch_yearly_data
import cdo_fetch_monthly_data_Copy1 as fetch_monthly_data



warnings.filterwarnings("ignore")

def save_fig(ds2_dict):
    for key, ds2 in ds2_dict.items():
        fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': ccrs.PlateCarree()})

        # Main plot: Contour plot of potential vorticity
        contour = ax.contourf(ds2.longitude, ds2.latitude, ds2.pvpot2[0, :, :], cmap="viridis")
        fig.colorbar(contour, ax=ax, orientation="vertical", label="PVPot")
        
        ax.coastlines(color='white', linewidth=0.7)
        ax.add_feature(cfeature.BORDERS, edgecolor='white', linewidth=0.5)
        
        gl = ax.gridlines(draw_labels=True, linestyle="None")
        gl.top_labels = False  # Disable top labels
        gl.right_labels = False  # Disable right labels
        gl.xlabel_style = {'size': 10, 'color': 'black'}
        gl.ylabel_style = {'size': 10, 'color': 'black'}

        plt.show()
        
        plt.savefig(f"monthly_plots/pvpot-{key}.png")


    
# location of era5 data on teachinghub
path="../../LEHRE/msc-intro-comp-met-ex-w2024/data/era5/"

parser = argparse.ArgumentParser()
# USAGE: python main.py --new_data monthly 1950
# USAGE: python main.py monthly 1950
parser.add_argument("--new_data", action="store_true", help="If you include --new_data, this will be true. If you omit it, it will be false")
parser.add_argument("timestep", type=str, choices=["monthly", "yearly"], help="Select the timestep, either 'monthly' or 'yearly'")
parser.add_argument("start_year", type=int, help="Specify the start year")
parser.add_argument("--end_year", type=int, help="Select the end year (optional). If no end year provided, only uses the start year")

args = parser.parse_args()

# TODO: change these two lines in arguments that allows you to set the date range
monthly = True # change this to False if you want yearly data

years = []
if args.end_year:
    years=list(range(args.start_year, args.end_year + 1))
else:
    years=[args.start_year]


if monthly:
    ds2_dict = fetch_monthly_data.fetch_monthly_data(path=path, new_data=args.new_data, years=years)
    Path("monthly_plots").mkdir(parents=True, exist_ok=True)
    save_fig(ds2_dict)
else:
    # THE YEARLY DATA DOESNT WORK YET! JUST WORK WITH MONTHLY DATA FOR NOW
    ds2=fetch_yearly_data.get_filelists(years,new_data=args.new_data)
    Path("yearly_plots").mkdir(parents=True, exist_ok=True)
    save_fig(ds2)



   


    
# fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': ccrs.PlateCarree()})

# # Main plot: Contour plot of potential vorticity
# contour = ax.contourf(ds2.longitude, ds2.latitude, ds2.pvpot2[0, :, :], cmap="viridis")
# fig.colorbar(contour, ax=ax, orientation="vertical", label="Potential Vorticity")

# ax.coastlines(color='white', linewidth=0.7)
# ax.add_feature(cfeature.BORDERS, edgecolor='white', linewidth=0.5)

# gl = ax.gridlines(draw_labels=True, linestyle="None")
# gl.top_labels = False  # Disable top labels
# gl.right_labels = False  # Disable right labels
# gl.xlabel_style = {'size': 10, 'color': 'black'}
# gl.ylabel_style = {'size': 10, 'color': 'black'}

# plt.show()
# if monthly: 
#     plt.savefig('monthly_plots/pvpot-1950-01.png')
# else:
#     plt.savefig('monthly_plots/pvpot-1950.png')