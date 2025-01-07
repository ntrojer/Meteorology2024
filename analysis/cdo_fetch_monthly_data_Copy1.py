'''import xarray as xr
from pathlib import Path
import pandas as pd
from cdo import Cdo
import core as core

# Temporäres Verzeichnis für CDO
tempPath = './tmp/'
cdo = Cdo(tempdir=tempPath)

def fetch_monthly_data(path, new_data, years):
    months = [f"{month:02}" for month in range(1, 13)]
    ds2_dict = {}

    # Temporäres Verzeichnis erstellen
    Path(tempPath).mkdir(parents=True, exist_ok=True)

    year = years[0]
    
    if new_data:
        Path(f"era5-{year}-monthly").mkdir(parents=True, exist_ok=True)
        for month in months:
            # Eingabedateipfad
            input_file = f"{path}era5-{year}-{month}.nc"
            
            # Öffnen der NetCDF-Datei
            ds2 = xr.open_mfdataset(input_file, chunks={"valid_time": 86400})
            
            # Berechnung von pvpot
            ds2["wspd"] = core.windspeed(ds2)
            ds2["pvpot2"] = core.pv_pot(ds2).compute()
            
            # Temporäre Datei mit berechnetem pvpot speichern
            temp_file_pvpot = f"{tempPath}temp-era5-{year}-{month}-pvpot.nc"
            ds2[["pvpot2", "longitude", "latitude"]].to_netcdf(temp_file_pvpot)
            
            # Zeitmittelwert mit CDO berechnen
            temp_file_timmean = cdo.timmean(input=temp_file_pvpot, returnFileName=True)
            
            # Ergebnis erneut öffnen
            ds2_mean = xr.open_dataset(temp_file_timmean)
            
            # Speichern der gewünschten Variablen in der finalen Datei
            output_file = f"era5-{year}-monthly/era5-{year}-{month}.nc"
            ds2_mean.to_netcdf(output_file)
            
            # Hinzufügen zum Dictionary
            ds2_dict[f"{year}-{month}"] = ds2_mean
            
            # Temporäre Dateien löschen
            Path(temp_file_pvpot).unlink()
    else:
        for month in months:
            # Öffnen der bereits existierenden Dateien
            ds2 = xr.open_dataset(f"era5-{year}-monthly/era5-{year}-{month}.nc")
            ds2_dict[f"{year}-{month}"] = ds2

    return ds2_dict'''

import xarray as xr
from pathlib import Path
import pandas as pd
from cdo import Cdo
import core as core

# Temporäres Verzeichnis für CDO
tempPath = './tmp/'
cdo = Cdo(tempdir=tempPath)

def fetch_monthly_data(path, new_data, years):
    months = [f"{month:02}" for month in range(1, 13)]
    ds2_dict = {}

    # Temporäres Verzeichnis erstellen
    Path(tempPath).mkdir(parents=True, exist_ok=True)

    # Gemeinsamer Speicherort für alle Jahre
    output_dir = "era5-20s"
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for year in years:  # Schleife über mehrere Jahre
        for month in months:
            # Eingabedateipfad
            input_file = f"{path}era5-{year}-{month}.nc"
            
            if new_data:
                # Öffnen der NetCDF-Datei
                ds2 = xr.open_mfdataset(input_file, chunks={"valid_time": 86400})
                
                # Berechnung von pvpot
                ds2["wspd"] = core.windspeed(ds2)
                ds2["pvpot2"] = core.pv_pot(ds2).compute()
                
                # Temporäre Datei mit berechnetem pvpot speichern
                temp_file_pvpot = f"{tempPath}temp-era5-{year}-{month}-pvpot.nc"
                ds2[["pvpot2", "longitude", "latitude"]].to_netcdf(temp_file_pvpot)
                
                # Zeitmittelwert mit CDO berechnen
                temp_file_timmean = cdo.timmean(input=temp_file_pvpot, returnFileName=True)
                
                # Ergebnis erneut öffnen
                ds2_mean = xr.open_dataset(temp_file_timmean)
                
                # Speichern der gewünschten Variablen in der finalen Datei
                output_file = f"{output_dir}/era5-{year}-{month}.nc"
                ds2_mean.to_netcdf(output_file)
                
                # Hinzufügen zum Dictionary
                ds2_dict[f"{year}-{month}"] = ds2_mean
                
                # Temporäre Dateien löschen
                Path(temp_file_pvpot).unlink()
            else:
                # Öffnen der bereits existierenden Dateien
                output_file = f"{output_dir}/era5-{year}-{month}.nc"
                ds2 = xr.open_dataset(output_file)
                ds2_dict[f"{year}-{month}"] = ds2

    return ds2_dict
    
path = "../../LEHRE/msc-intro-comp-met-ex-w2024/data/era5/"  # Pfad zu den NetCDF-Eingabedateien
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]  # Liste der Jahre
new_data = True  # Setze auf False, um nur vorhandene Dateien zu laden

ds2_dict = fetch_monthly_data(path=path, new_data=new_data, years=years)
