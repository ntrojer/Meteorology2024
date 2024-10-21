# call with:
# /srvfs/home/avoigt/micromamba/envs/intro-comp-meteo-ex-w2024/bin/python3.10 era5-download.py

import numpy as np
import download as download

# define list of years 
ystart=2000;
yend=2010;
years=[];
[years.append(str(year)) for year in np.arange(ystart,yend+1)];

# define list of months
months = ["01","02","03","04","05","06","07","08","09","10","11","12"];

for year in years:
    for month in months:
        download.era5(year, month)