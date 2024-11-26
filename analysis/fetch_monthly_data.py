import xarray as xr
import core as core
from pathlib import Path


def fetch_monthly_data(path, new_data, years):
    months = [f"{month:02}" for month in range(1, 13)]
    ds2_dict = {}

    # TODO: make this handle a list of years
    year=years[0] 
    
    if new_data:
        Path(f"era5-{year}-monthly").mkdir(parents=True, exist_ok=True)
        for month in months:
            ds2=xr.open_mfdataset(path + f"era5-{year}-{month}.nc", chunks={"valid_time":1e5} )
            ds2["wspd"] = core.windspeed(ds2)
            ds2["pvpot2"] = core.pv_pot(ds2).groupby(ds2.valid_time.dt.month).mean("valid_time").compute()
            # pvpot2 = core.pv_pot(ds2).groupby(ds2.valid_time.dt.month).mean("valid_time").compute()
            ds2[["pvpot2", "longitude", "latitude"]].to_netcdf(f"era5-{year}-monthly/era5-{year}-{month}.nc")
            
            ds2_dict[f"{year}-{month}"] = ds2
    else:
        for month in months:
            ds2 = xr.open_dataset(f"era5-{year}-monthly/era5-{year}-{month}.nc")

            ds2_dict[f"{year}-{month}"] = ds2

    return ds2_dict