# call with:
# /srvfs/home/avoigt/micromamba/envs/intro-comp-meteo-ex-w2024/bin/python3.10 era5-land-download.py

import xarray as xr
import cdsapi

import cdsapi

dataset = "reanalysis-era5-land"
request = {
    "variable": [
        "2m_temperature",
        "surface_solar_radiation_downwards",
        "10m_u_component_of_wind",
        "10m_v_component_of_wind"
    ],
    "year": "1950",
    "month": "01",
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ],
    "time": [
        "00:00", "01:00", "02:00",
        "03:00", "04:00", "05:00",
        "06:00", "07:00", "08:00",
        "09:00", "10:00", "11:00",
        "12:00", "13:00", "14:00",
        "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00",
        "21:00", "22:00", "23:00"
    ],
    "data_format": "netcdf",
    "download_format": "unarchived"
}

client = cdsapi.Client()
client.retrieve(dataset, request).download("/srvfs/scratch/avoigt/msc-intro-computational-meteorology-exercises-w2024/era5-land-1950-01.nc")