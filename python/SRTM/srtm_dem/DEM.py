"""

    module DEM.py

    Opens binary '.hgt' DEM files and converts to a 2D numpy array

    Download SRTM files from the ftp server
    https://dds.cr.usgs.gov/srtm/version2_1/SRTM3/North_America/

"""

import os

import numpy as np
from matplotlib import pyplot as plt

import filemanager

_fill = -32768

class DEM:
    _samples = 1201
    _shape = (_samples, _samples)
    def __init__(self, lat, lon):
        ilat, ilon = int(np.floor(lat)), int(np.floor(lon))
        dem_file = filemanager.get_dem_path(lat, lon)
        if not os.path.exists(dem_file):
            print("Downloading file %s" % dem_file)
            filemanager.download(lat, lon)
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
        return self.elevations[lat_row, lon_col]
