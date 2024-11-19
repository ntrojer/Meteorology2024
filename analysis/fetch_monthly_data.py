import xarray as xr
import core as core
from pathlib import Path


def fetch_monthly_data(path, new_data):
    if new_data:
        Path("era5-1950-monthly").mkdir(parents=True, exist_ok=True)
    
        ds2=xr.open_mfdataset(path + "era5-1950-01.nc", chunks={"valid_time":1e5} )
        ds2["wspd"] = core.windspeed(ds2)
        ds2["pvpot2"] = core.pv_pot(ds2).groupby(ds2.valid_time.dt.month).mean("valid_time").compute()
        # pvpot2 = core.pv_pot(ds2).groupby(ds2.valid_time.dt.month).mean("valid_time").compute()
        ds2[["pvpot2", "longitude", "latitude"]].to_netcdf("era5-1950-monthly/era5-1950-01.nc")
    else:
        ds2 = xr.open_dataset("era5-1950-monthly/era5-1950-01.nc")

    return ds2