# MSc Intro Computational Meteorology Exercises W2024

Git repo for the exercises.

Directory structure:
 
 * `organisational`: information on the content of the exercises and to get started with the data analysis
 * `python-kernel`: create python kernel on IMG Teachinghub via the Masterhub access, using the account avoigt
 * `era5-download`: scripts to retrieve ERA5 and ERA5-Land data from the Copernicus Data Store
 * `analysis`: scripts to calculate PV potential etc.

Notes for Aiko Voigt:

 * The ERA5 and ERA5-Land download scripts need to be executed logged in as avoigt to the Masterhub via wolke.img.univie.ac.at. The data will be put in a directory only accessible to avoigt.
 * Then, the data can be copied to `/stufs/lehre/msc-intro-comp-met-ex-w2024/data/`. There, it is accessible to everybody logged in via the Moodle Teachinghub under `LEHRE/msc-intro-comp-met-ex-w2024/data/`.

#for NINA:
#git status
#git add analysis/
#git commit -m "change"
#git push

#git pull origin main #to see the changes of the others

Projects: 
* Start with monthly climatology of pv pot (want to do)
* Europe: to satisfy Europe's energy, how much area needs to be covered by PV, and where?
* PV pot change between 1950-1959 and 2000-2009; climate chnage singnal?  (want to do)
* PV pot and extrem event (are there some correlations?)
* If we have time: How PV pot changes, if we would have only daily data and not hourly data (calculate the mean data for one day) (could als try to do it "bachwards" with machine learning, as we have the hourly data)

Next: 
* argument for false and true for data loading (Now for new data: python main.py --new_data)
* PVpot for each month over one year, that we can see how it changes with the seasons (12 plots)-year: 2005
      (montly 2.9 GB was big so we should take the annual mean or we try until there is no space for saving anymore)
* Write comments ;)
* Save data for every year-> 1950-1959 and of 2000-2010
* -> Plot the mean of 1950-1959 and of 2000-2010 (2 plots)
* -> Same for all four seasons (8 plots): mean over all years for the seasons
* Continents (e.g. Antarctica)

DONE:
* plot the data with map
* save the data in netcdf file *


Changes:
main.py:
path = "../../Meteorology2024/analysis/"
if args.timestep == "monthly":
    ds2_m = fetch_monthly_data.fetch_monthly_data(path=path, new_data=args.new_data, years=years)
    #Path("monthly_plots").mkdir(parents=True, exist_ok=True)
    save_fig(ds2_m, timestep="monthly")
elif args.timestep == "yearly":
    ds2_y = fetch_yearly_data.fetch_yearly_data(path=path, new_data=args.new_data, years=years)
    save_fig(ds2_y, timestep="yearly")

fetch_yearly_data:
import xarray as xr
import core as core
from pathlib import Path

def fetch_yearly_data(path, new_data, years):
    ds2_dict = {}
    for year in years:
        if new_data:
            Path(f"era5-{year}-yearly").mkdir(parents=True, exist_ok=True)
            ds = xr.open_mfdataset(
                f"{path}era5-{year}-*.nc",
                combine="by_coords",
                chunks={"valid_time": 1e5}
            )
            ds["wspd"] = core.windspeed(ds)
            ds["pvpot2"] = core.pv_pot(ds).mean(dim="valid_time").compute()
            ds[["pvpot2", "longitude", "latitude"]].to_netcdf(f"era5-{year}-yearly/era5-{year}.nc")
            ds2_dict[str(year)] = ds
        else:
            path= "../../Meteorology2024/analysis/"
            yearly_file = f"era5-{year}.nc"
            if Path(yearly_file).exists():
                ds = xr.open_dataset(yearly_file)
                ds2_dict[str(year)] = ds
            else:
                raise FileNotFoundError(f"Yearly file {yearly_file} does not exist. Use --new_data to generate it.")

    return ds2_dict













Presentation:
Thema                                   Person
Motivation/ aim /project question       Mimi
Dataset -> netcdf                       Julia
Yearly and monthly plots                Julia
Machine Learning                        Mimi

Results:
- Show the plots and video              Nina
- Monat difference different plots      Nina

Conclusion
- Difference yearly one plot            Nina
- answer the question climate change    Nina
 (one plot for 10 years for the differnce)










