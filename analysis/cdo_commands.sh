cdo mergetime era5-* era5-1959.nc (für jedes Jahr also 10 mal, einzelnd in  den ordnern)
cdo mergetime era5-* era5-19s.nc (die einzelnen Jahre zusammen gemerged in einem neuen Ordner(era5_19_yearly))
cdo yearmean era5-19s.nc era5-19s-ym.nc (jahresmittel (10 Jahresskala))
cdo ymonmean era5-19s.nc era5-19s-ymon.nc () jahresgang gemittelt über die zehn Jahre, also jeweils die Monate einzelnd(Monatsskala))
cdo fldmean era5-20s-ym.nc  era5-20s-ym-globalmean.nc (globales mittel)
cdo zonmean era5-19s-ymon.nc era5-19s-ymon-zm.nc
cdo zonmean era5-19s-ym.nc era5-19s-ym-zm.nc