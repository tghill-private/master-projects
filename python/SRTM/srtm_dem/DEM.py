"""

    module DEM.py

    Opens binary '.hgt' DEM files and converts to a 2D numpy array

    Download SRTM files from the ftp server
    https://dds.cr.usgs.gov/srtm/version2_1/SRTM3/North_America/

"""

import os

import numpy as np
from matplotlib import pyplot as plt

file_path = "dem/{lat}{lon}.hgt"

_fill = -32768

def get_dem_path(lat, lon):
    lat_str = "N%s"%int(np.floor(lat)) if lat>=0 else "S%s"%int(abs(np.floor(lat)))
    lon_str = "E%s"%int(np.floor(lon)) if lon>=0 else "W%.3d"%int(abs(np.floor(lon)))
    path = file_path.format(lat=lat_str, lon=lon_str)
    return path

class DEM:
    _samples = 1201
    _shape = (_samples, _samples)
    def __init__(self, lat, lon):
        ilat, ilon = int(np.floor(lat)), int(np.floor(lon))
        dem_file = get_dem_path(lat, lon)
        with open(dem_file, 'r') as dem:
            elevations = np.fromfile(dem, dtype=np.dtype('>i2')).reshape(DEM._shape).astype(int)
        lats = np.linspace(ilat+1, ilat, DEM._samples)
        lons = np.linspace(ilon, ilon+1, DEM._samples)
        latlon = np.meshgrid(lons, lats)

        self.elevations = np.ma.masked_equal(elevations, _fill)
        self.latlon = latlon
        self.latitudes = lats
        self.longitudes = lons

        self.srtm_dem = os.path.split(dem_file)[1]

    def __getitem__(self, coord):
        lat, lon = coord
        lat_row = int(np.floor((lat - int(lat)) * (DEM._samples - 1)))
        lat_row = DEM._samples - 1 - lat_row
        lon_col = int(np.floor( (lon - int(lon)) * (DEM._samples - 1)))

        # latlon_chk = (self.latlon[0][lat_row, lon_col], self.latlon[1][lat_row, lon_col])
        #
        # print latlon_chk
        return self.elevations[lat_row, lon_col]


# def main():
#     fig, ax = plt.subplots()
#
#     dem = DEM(44.51, -80.3)
#     color_plot = ax.pcolormesh(dem.latlon[0], dem.latlon[1][::-1], dem.elevations[::-1])
#
#     ax.set_xlim(dem.longitudes[0], dem.longitudes[-1])
#     ax.set_ylim(dem.latitudes[-1], dem.latitudes[0])
#
#     cbar = fig.colorbar(color_plot)
#
#     cbar.set_label("Elevation (m)")
#
#     title = os.path.splitext(dem.srtm_dem)[0]
#     ax.set_title(title)
#
#     ax.set_xlabel("Longitude ($^{\circ}$E)")
#     ax.set_ylabel("Latitude ($^{\circ}$N)")
#
#     ax.grid()
#     fig.savefig('../Images/{}.png'.format(dem.srtm_dem), dpi=600)
#
if __name__ == "__main__":
    main()
