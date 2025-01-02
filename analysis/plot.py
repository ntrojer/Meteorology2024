import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

file_path_ymon_20 = "era5-20s/era5-20s-ymon-globalmean.nc"  
ds_ymon_20 = xr.open_dataset(file_path_ymon_20)

file_path_ymon_19 = "era5_19_yearly/era5-19s-ymon-globalmean.nc"  
ds_ymon_19 = xr.open_dataset(file_path_ymon_19)

file_path_ym_20 = "era5-20s/era5-20s-ym-globalmean.nc"  
ds_ym_20 = xr.open_dataset(file_path_ym_20)

file_path_ym_19 = "era5_19_yearly/era5-19s-ym-globalmean.nc"  
ds_ym_19 = xr.open_dataset(file_path_ym_19)

file_path_zm_20 = "era5-20s/era5-20s-ymon-zm.nc"  
ds_zm_20 = xr.open_dataset(file_path_zm_20)

file_path_zm_19 = "era5_19_yearly/era5-19s-ymon-zm.nc"  
ds_zm_19 = xr.open_dataset(file_path_zm_19)

file_path_ym_zm_20 = "era5-20s/era5-20s-ym-zm.nc"  
ds_ym_zm_20 = xr.open_dataset(file_path_ym_zm_20)

file_path_ym_zm_19 = "era5_19_yearly/era5-19s-ym-zm.nc"  
ds_ym_zm_19 = xr.open_dataset(file_path_ym_zm_19)

file_path_t2m_greenland = "era5_t2m_19_ymon_greenland.nc"  
ds_t2m_gl = xr.open_dataset(file_path_t2m_greenland)

file_path_pvpot_greenland = "era5_19_ymon_greenland.nc"  
ds_pvpot_gl= xr.open_dataset(file_path_pvpot_greenland)

file_path_ssrd_greenland = "era5_ssrd_19_ymon_greenland.nc"  
ds_ssrd_gl = xr.open_dataset(file_path_ssrd_greenland)

file_path_t2m_austria = "era5_t2m_19_ymon_greenland.nc"  
ds_t2m_aut = xr.open_dataset(file_path_t2m_austria)

file_path_pvpot_austria = "era5_19_ymon_austria.nc"  
ds_pvpot_aut= xr.open_dataset(file_path_pvpot_austria)

file_path_ssrd_austria = "era5_ssrd_19_ymon_austria.nc"  
ds_ssrd_aut = xr.open_dataset(file_path_ssrd_austria)


# ---------------- Globales Mittel (ymon) ---------------------------

# Extrahiere die gewünschte Variable (z. B. 'pvpot2') als DataArray
pvpot_20 = ds_ymon_20['pvpot2']
pvpot_19 = ds_ymon_19['pvpot2']

# Konvertiere die Werte in ein numpy-Array (1D- oder 2D-Struktur)
pvpot_values_20 = pvpot_20.values.squeeze()  # Entfernt überflüssige Dimensionen, falls nötig
pvpot_values_19 = pvpot_19.values.squeeze()

# Anzahl der Jahre (entspricht der Zeitdimension)
num_years_20 = pvpot_values_20.shape[0]
num_years_19 = pvpot_values_19.shape[0]

# Plotting the PVPot monthly mean over the year 1950
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the monthly mean potential vorticity
ax.plot(range(1, num_years_19 + 1), pvpot_values_19, marker='o', color='r', linestyle='-', markersize=6, label="1950-1959")
ax.plot(range(1, num_years_20 + 1), pvpot_values_20, marker='o', color='b', linestyle='-', markersize=6, label="2000-2009")


# Add labels and title
ax.set_title("Mean PVPot for each Month: 1950-1959 and 2000-2009", fontsize=16)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Global Mean PVPot", fontsize=12)

# Add gridlines and customize the x-axis to show month names
ax.set_xticks(range(1, num_years_20 + 1))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

ax.legend(fontsize=12)

# Save the plot
plt.savefig("pvpot-ymon-globalmean.png")

# Display the plot
plt.show()

# ---------------- Globales Mittel (ym) ---------------------------

# Extrahiere die gewünschte Variable (z. B. 'pvpot2') als DataArray
pvpot_20 = ds_ym_20['pvpot2']
pvpot_19 = ds_ym_19['pvpot2']

# Konvertiere die Werte in ein numpy-Array (1D- oder 2D-Struktur)
pvpot_values_20 = pvpot_20.values.squeeze()  # Entfernt überflüssige Dimensionen, falls nötig
pvpot_values_19 = pvpot_19.values.squeeze()

# Anzahl der Jahre (entspricht der Zeitdimension)
num_years_20 = pvpot_values_20.shape[0]
num_years_19 = pvpot_values_19.shape[0]

# Plotting the PVPot monthly mean over the year 1950
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the monthly mean potential vorticity
ax.plot(range(1, num_years_19 + 1), pvpot_values_19, marker='o', color='r', linestyle='-', markersize=6, label="1950-1959")
ax.plot(range(1, num_years_20 + 1), pvpot_values_20, marker='o', color='b', linestyle='-', markersize=6, label="2000-2009")

# Add labels and title
ax.set_title("Mean PVPot for Each Year: 1950-1959 and 2000-2009", fontsize=16)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Global Mean PVPot", fontsize=12)

ax.set_xticks(range(1, num_years_20 + 1))

# Kombiniere die Jahreszahlen in einem Label mit Zeilenumbrüchen
combined_labels = [
    '1950\n2000', '1951\n2001', '1952\n2002', '1953\n2003', '1954\n2004',
    '1955\n2005', '1956\n2006', '1957\n2007', '1958\n2008', '1959\n2009'
]

ax.set_xticklabels(combined_labels)

ax.legend(fontsize=12)

# Save the plot
plt.savefig("pvpot-ym-globalmean.png")

# Display the plot
plt.show()

# ---------------------------------- Zonmean (zonales Mittel ymon) --------------------------------------
# Extrahiere die zonal gemittelten Hovmöller-Daten
hovmoller_19 = ds_zm_19['pvpot2'].squeeze()  # Zonal gemittelte Daten für 1950-1959
hovmoller_20 = ds_zm_20['pvpot2'].squeeze()  # Zonal gemittelte Daten für 2000-2009

# Setze alle Werte kleiner als 0 auf 0
hovmoller_19 = hovmoller_19.where(hovmoller_19 >= 0, 0)
hovmoller_20 = hovmoller_20.where(hovmoller_20 >= 0, 0)

# --- Set rangs of values to be plotted of Reff
clevs = np.arange(0.0, 0.56, 0.025)
    
# Erstellen des Plots
fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Monatsnamen für die x-Achse
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Hovmöller-Diagramm für 1950-1959
im1 = axes[0].contourf(
    range(1, 13),  # 12 Monate
    hovmoller_19['lat'], 
    hovmoller_19.T,  # Transponieren, damit y = Breite und x = Monate
    cmap='coolwarm',
    levels=clevs
)
axes[0].set_title("Hovmöller Diagram: 1950-1959", fontsize=16)
axes[0].set_ylabel("Latitude", fontsize=12)
axes[0].set_xticks(range(1, 13))  # Monatliche Skala (1-12)
axes[0].set_xticklabels(months)  # Monatsnamen (Jan-Dec)
fig.colorbar(im1, ax=axes[0], orientation='vertical', label='PVPot')

# Hovmöller-Diagramm für 2000-2009
im2 = axes[1].contourf(
    range(1, 13),  # 12 Monate
    hovmoller_20['lat'], 
    hovmoller_20.T,  # Transponieren, damit y = Breite und x = Monate
    cmap='coolwarm',
    levels=clevs
)
axes[1].set_title("Hovmöller Diagram: 2000-2009", fontsize=16)
axes[1].set_xlabel("Month", fontsize=12)
axes[1].set_ylabel("Latitude", fontsize=12)
axes[1].set_xticks(range(1, 13))  # Monatliche Skala (1-12)
axes[1].set_xticklabels(months)  # Monatsnamen (Jan-Dec)
fig.colorbar(im2, ax=axes[1], orientation='vertical', label='PVPot')

# Layout anpassen und Plot speichern
plt.tight_layout()
plt.savefig("hovmoller_pvpot_ymon.png")

# Anzeigen
plt.show()


# ---------------------------------- Zonmean (zonales Mittel ym) --------------------------------------

# Extrahiere die zonal gemittelten Hovmöller-Daten
hovmoller_19_ym = ds_ym_zm_19['pvpot2'].squeeze()  # Entfernt überflüssige Dimensionen
hovmoller_20_ym = ds_ym_zm_20['pvpot2'].squeeze()  # Entfernt überflüssige Dimensionen

vmin = min(hovmoller_19_ym.min(), hovmoller_20_ym.min())
vmax = max(hovmoller_19_ym.max(), hovmoller_20_ym.max())

# --- Set rangs of values to be plotted of Reff
clevs = np.arange(0.08, 0.24, 0.0001)

# Erstellen des Plots
fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=False)

# Jahre für die x-Achse
years_19 = [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959]
years_20 = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]  
 

# Hovmöller-Diagramm für 1950-1959
im1 = axes[0].contourf(
    range(1, 11),  # Zeit (Jahre)
    hovmoller_19_ym['lat'], 
    hovmoller_19_ym.T,  # `.values.T` liefert die transponierten reinen Werte
    cmap='coolwarm', 
    levels=clevs
)
axes[0].set_title("Hovmöller Diagram: 1950-1959", fontsize=16)
axes[0].set_ylabel("Latitude", fontsize=12)
axes[0].set_xticks(range(1, 11))  
axes[0].set_xticklabels(years_19)
fig.colorbar(im1, ax=axes[0], orientation='vertical', label='PVPot')


# Hovmöller-Diagramm für 2000-2009
im2 = axes[1].contourf(
    range(1, 11),  # Zeit (Jahre)
    hovmoller_20_ym['lat'], 
    hovmoller_20_ym.T,  # `.values.T` liefert die transponierten reinen Werte
    cmap='coolwarm',
    levels=clevs
)
axes[1].set_title("Hovmöller Diagram: 2000-2009", fontsize=16)
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Latitude", fontsize=12)
axes[1].set_xticks(range(1, 11))  
axes[1].set_xticklabels(years_20)
fig.colorbar(im2, ax=axes[1], orientation='vertical', label='PVPot')

# Layout anpassen und Plot speichern
plt.tight_layout()
plt.savefig("hovmoller_pvpot_ym.png")

# Anzeigen
plt.show()

# ---------------- Greenland t2m/pvpot ---------------------------

# Extrahiere die gewünschte Variable (z. B. 'pvpot2') als DataArray
t2m_gl = ds_t2m_gl['t2m'] - 273.15
pvpot_gl = ds_pvpot_gl['pvpot2']

# Konvertiere die Werte in ein numpy-Array (1D- oder 2D-Struktur)
t2m_gl = t2m_gl.values.squeeze()  # Entfernt überflüssige Dimensionen, falls nötig
pvpot_gl = pvpot_gl.values.squeeze()

# Anzahl der Jahre (entspricht der Zeitdimension)
t2m_gl_month = t2m_gl.shape[0]
pvpot_gl_month = pvpot_gl.shape[0]

# Erstellen des Plots mit zwei y-Achsen
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot für PVPot auf der linken y-Achse
ax1.plot(range(1, pvpot_gl_month + 1), pvpot_gl, marker='o', color='r', linestyle='-', markersize=6, label="PVPot")
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Greenland Mean PVPot", color='r', fontsize=12)
ax1.tick_params(axis='y', labelcolor='r')

# Erstellen der zweiten y-Achse für Temperatur
ax2 = ax1.twinx()
ax2.plot(range(1, t2m_gl_month + 1), t2m_gl, marker='o', color='b', linestyle='-', markersize=6, label="t2m")
ax2.set_ylabel("Greenland Mean t2m (°C)", color='b', fontsize=12)
ax2.tick_params(axis='y', labelcolor='b')

# Gemeinsame x-Achse
ax1.set_xticks(range(1, pvpot_gl_month + 1))
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Titel und Legende
fig.suptitle("Mean PVPot and t2m for Each Month: Greenland", fontsize=16)
fig.tight_layout()

# Speichern und Anzeigen des Plots
plt.savefig("pvpot-t2m-greenland.png")
plt.show()

# ---------------- Austria t2m/pvpot ---------------------------

# Extrahiere die gewünschte Variable (z. B. 'pvpot2') als DataArray
t2m_aut = ds_t2m_aut['t2m'] - 273.15
pvpot_aut = ds_pvpot_aut['pvpot2']


# Konvertiere die Werte in ein numpy-Array (1D- oder 2D-Struktur)
t2m_aut = t2m_aut.values.squeeze()  # Entfernt überflüssige Dimensionen, falls nötig
pvpot_aut = pvpot_aut.values.squeeze()

# Anzahl der Jahre (entspricht der Zeitdimension)
t2m_aut_month = t2m_aut.shape[0]
pvpot_aut_month = pvpot_aut.shape[0]

# Erstellen des Plots mit zwei y-Achsen
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot für PVPot auf der linken y-Achse
ax1.plot(range(1, pvpot_aut_month + 1), pvpot_aut, marker='o', color='r', linestyle='-', markersize=6, label="PVPot")
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Austria Mean PVPot", color='r', fontsize=12)
ax1.tick_params(axis='y', labelcolor='r')

# Erstellen der zweiten y-Achse für Temperatur
ax2 = ax1.twinx()
ax2.plot(range(1, t2m_aut_month + 1), t2m_aut, marker='o', color='b', linestyle='-', markersize=6, label="t2m")
ax2.set_ylabel("Austria Mean t2m (°C)", color='b', fontsize=12)
ax2.tick_params(axis='y', labelcolor='b')

# Gemeinsame x-Achse
ax1.set_xticks(range(1, pvpot_aut_month + 1))
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Titel und Legende
fig.suptitle("Mean PVPot and t2m for Each Month: Austria", fontsize=16)
fig.tight_layout()

# Speichern und Anzeigen des Plots
plt.savefig("pvpot-t2m-austria.png")
plt.show()

# ---------------- Austria t2m/pvpot/ssrd ---------------------------

# Extrahiere die gewünschte Variable (z. B. 'pvpot2') als DataArray
t2m_aut = ds_t2m_aut['t2m'] - 273.15
pvpot_aut = ds_pvpot_aut['pvpot2']
ssrd_aut = ds_ssrd_aut['ssrd']/3600


# Konvertiere die Werte in ein numpy-Array (1D- oder 2D-Struktur)
t2m_aut = t2m_aut.values.squeeze()  # Entfernt überflüssige Dimensionen, falls nötig
pvpot_aut = pvpot_aut.values.squeeze()
ssrd_aut = ssrd_aut.values.squeeze()

# Anzahl der Jahre (entspricht der Zeitdimension)
t2m_aut_month = t2m_aut.shape[0]
pvpot_aut_month = pvpot_aut.shape[0]

# Erstellen des Plots mit zwei y-Achsen
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot für PVPot auf der linken y-Achse
ax1.plot(range(1, pvpot_aut_month + 1), pvpot_aut, marker='o', color='r', linestyle='-', markersize=6, label="PVPot")
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Austria Mean PVPot", color='r', fontsize=12)
ax1.tick_params(axis='y', labelcolor='r')

# Erstellen der zweiten y-Achse für Temperatur
ax2 = ax1.twinx()
ax2.plot(range(1, t2m_aut_month + 1), t2m_aut, marker='o', color='b', linestyle='-', markersize=6, label="t2m")
ax2.set_ylabel("Austria Mean t2m (°C)", color='b', fontsize=12)
ax2.tick_params(axis='y', labelcolor='b')

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("outward", 60))  # Verschiebt die dritte Achse nach rechts
ax3.plot(range(1, t2m_aut_month + 1), ssrd_aut, marker='o', color='g', linestyle='-', markersize=6, label="ssrd")
ax3.set_ylabel("Austria Mean SSRD (W/m²)", color='g', fontsize=12)
ax3.tick_params(axis='y', labelcolor='g')

# Gemeinsame x-Achse
ax1.set_xticks(range(1, pvpot_aut_month + 1))
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Titel und Legende
fig.suptitle("Mean PVPot, ssrd and t2m for Each Month: Austria", fontsize=16)
fig.tight_layout()

# Speichern und Anzeigen des Plots
plt.savefig("pvpot-t2m-ssrd-austria.png")
plt.show()

# ---------------- Greenland t2m/pvpot/ssrd ---------------------------

# Extrahiere die gewünschte Variable (z. B. 'pvpot2') als DataArray
t2m_gl = ds_t2m_gl['t2m'] - 273.15
pvpot_gl = ds_pvpot_gl['pvpot2']
ssrd_gl = ds_ssrd_gl['ssrd']/3600


# Konvertiere die Werte in ein numpy-Array (1D- oder 2D-Struktur)
t2m_gl = t2m_gl.values.squeeze()  # Entfernt überflüssige Dimensionen, falls nötig
pvpot_gl = pvpot_gl.values.squeeze()
ssrd_gl = ssrd_gl.values.squeeze()

# Anzahl der Jahre (entspricht der Zeitdimension)
t2m_gl_month = t2m_gl.shape[0]
pvpot_gl_month = pvpot_gl.shape[0]

# Erstellen des Plots mit zwei y-Achsen
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot für PVPot auf der linken y-Achse
ax1.plot(range(1, pvpot_gl_month + 1), pvpot_gl, marker='o', color='r', linestyle='-', markersize=6, label="PVPot")
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Greenland Mean PVPot", color='r', fontsize=12)
ax1.tick_params(axis='y', labelcolor='r')

# Erstellen der zweiten y-Achse für Temperatur
ax2 = ax1.twinx()
ax2.plot(range(1, t2m_gl_month + 1), t2m_gl, marker='o', color='b', linestyle='-', markersize=6, label="t2m")
ax2.set_ylabel("Greenland Mean t2m (°C)", color='b', fontsize=12)
ax2.tick_params(axis='y', labelcolor='b')

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("outward", 60))  # Verschiebt die dritte Achse nach rechts
ax3.plot(range(1, t2m_gl_month + 1), ssrd_gl, marker='o', color='g', linestyle='-', markersize=6, label="ssrd")
ax3.set_ylabel("Greenland Mean SSRD (W/m²)", color='g', fontsize=12)
ax3.tick_params(axis='y', labelcolor='g')

# Gemeinsame x-Achse
ax1.set_xticks(range(1, pvpot_gl_month + 1))
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Titel und Legende
fig.suptitle("Mean PVPot, ssrd and t2m for Each Month: Greenland", fontsize=16)
fig.tight_layout()

# Speichern und Anzeigen des Plots
plt.savefig("pvpot-t2m-ssrd-greenland.png")
plt.show()