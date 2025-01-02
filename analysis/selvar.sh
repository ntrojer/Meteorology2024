#!/bin/bash
 
YEARS=1950
for YEAR in {1950..1959..01}; do
for MONTHS in {01..12..01}; do

#cdo -fldmean -sellonlatbox,10,20,45,50 -selvar,t2m /home/kornbluehm52/LEHRE/msc-intro-comp-met-ex-w2024/data/era5/era5-${YEAR}-${MONTHS}.nc t1-${YEAR}-${MONTHS}.nc#
cdo -monmean -selvar,ssrd /home/kornbluehm52/LEHRE/msc-intro-comp-met-ex-w2024/data/era5/era5-${YEAR}-${MONTHS}.nc t1-${YEAR}-${MONTHS}.nc
#cdo -setctomiss,0 -mul t1-${YEAR}-${MONTHS}.nc /home/kornbluehm52/LEHRE/msc-intro-comp-met-ex-w2024/data/era5/era5_landseamask.nc t2-${YEAR}-${MONTHS}.nc
done
done

cdo -ymonmean -mergetime t1*.nc era5_ssrd_{YEARS}_ymonm.nc
#cdo mergetime t2*.nc era5_t2m_{YEARS}_land.nc

rm t[12]-*.nc 