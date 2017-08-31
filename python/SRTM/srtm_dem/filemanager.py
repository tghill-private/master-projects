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

def fetch_coords(lat_range, lon_range):
    """Returns coordinates for all data within the lat and lon ranges
    """
    lats = np.arange(lat_range[0], lat_range[1], 1.).astype(int)
    lons = np.arange(lon_range[0], lon_range[1], 1.).astype(int)

    # Catch case where only one file is required
    if len(lats)==0:
        lats = [lat_range[0]]
    if len(lons)==0:
        lons = [lon_range[0]]

    posns = np.array([ [(lat, lon) for lon in lons] for lat in lats[::-1] ])
    return posns

def download(lat, lon):
    dem_file = get_dem_file(lat, lon)
    if os.path.exists(get_dem_path(lat, lon)):
        print("File %s already exists" % dem_file)
    else:
        dem_zip = dem_file + '.zip'
        url = os.path.join(base_url, dem_zip)

        request = requests.get(url)
        status = request.status_code
        if status == requests.codes.not_found:
            raise IOError("The lat/lon (%s, %s) were not found" % (lat, lon))
        elif status == requests.codes.ok:
            bytes_data = io.BytesIO(request.content)
            with zipfile.ZipFile(bytes_data, 'r') as zip_ref:
                zip_ref.extractall('dem')
                zip_ref.close()
            print("File %s downloaded successfully" % dem_file)
        else:
            raise Exception("An uknown error occured while fetching file")

download(31, -110)
