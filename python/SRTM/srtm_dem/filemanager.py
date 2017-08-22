"""

module for downloading files from the ftp server
https://dds.cr.usgs.gov/srtm/version2_1/SRTM3/North_America/

"""

import os
import io
import zipfile

import numpy as np
import requests

file_path = "{lat}{lon}.hgt"

base_url = "https://dds.cr.usgs.gov/srtm/version2_1/SRTM3/North_America/"

save_dir = "dem"

def get_dem_file(lat, lon):
    lat_str = "N%s"%int(np.floor(lat)) if lat>=0 else "S%s"%int(abs(np.floor(lat)))
    lon_str = "E%s"%int(np.floor(lon)) if lon>=0 else "W%.3d"%int(abs(np.floor(lon)))
    path = file_path.format(lat=lat_str, lon=lon_str)
    return path

def get_dem_path(lat, lon):
    return os.path.join(save_dir, get_dem_file(lat, lon))

def download(lat, lon):
    dem_file = get_dem_file(lat, lon)
    dem_zip = dem_file + '.zip'
    url = os.path.join(base_url, dem_zip)

    request = requests.get(url)
    bytes_data = io.BytesIO(request.content)
    with zipfile.ZipFile(bytes_data, 'r') as zip_ref:
        zip_ref.extractall('dem')
        zip_ref.close()

    print "Done"

for lon in (-79, -80, -81):
    download(42, lon)
