import xarray as xr
import pandas as pd
import core as core

def process_existing_nc_file(input_nc_file, hourly_csv_file, daily_csv_file):
    """
    Verarbeitet bestehende monatliche NetCDF-Dateien mit stündlichen Daten.
    Erstellt CSV-Dateien für stündliche und tägliche Daten.
    Args:
        input_nc_file (str): Pfad zur bestehenden monatlichen NetCDF-Datei.
        hourly_csv_file (str): Pfad zur Ausgabe-CSV-Datei mit stündlichen Daten.
        daily_csv_file (str): Pfad zur Ausgabe-CSV-Datei mit täglichen Daten.
    """
    # NetCDF-Daten laden
    ds = xr.open_dataset(input_nc_file)
    
    # Zusätzliche Variablen berechnen (falls notwendig)
    if "wspd" not in ds:
        ds["wspd"] = core.windspeed(ds)
    if "pvpot" not in ds:
        ds["pvpot"] = core.pv_pot(ds)
    
    # In Pandas DataFrame umwandeln
    df = ds[["valid_time", "t2m", "pvpot", "longitude", "latitude"]].to_dataframe().reset_index()
    
    # Speichere stündliche Daten
    df.to_csv(hourly_csv_file, index=False)
    print(f"Stündliche Daten gespeichert unter: {hourly_csv_file}")
    
    # Tagesmittelwerte berechnen
    df["valid_time"] = pd.to_datetime(df["valid_time"])
    df["day"] = df["valid_time"].dt.date
    daily_df = df.groupby("day").mean().reset_index()
    
    # Speichere tägliche Mittelwerte
    daily_df.to_csv(daily_csv_file, index=False)
    print(f"Tägliche Mittelwerte gespeichert unter: {daily_csv_file}")


input_nc_file = "/home/kornbluehm52/LEHRE/msc-intro-comp-met-ex-w2024/data/era5/era5-1950-01.nc"
hourly_csv_file = "ml_data_hourly.csv"
daily_csv_file = "ml_data_daily.csv"

process_existing_nc_file(input_nc_file, hourly_csv_file, daily_csv_file)
