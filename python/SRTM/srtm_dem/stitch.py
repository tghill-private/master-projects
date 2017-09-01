"""

Module stitch.py

Stitches multiple files together into one DEM object.

"""

import numpy as np

import DEM

_res_limit = 4000

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

def stitch(files):
    global_elev = np.array([])
    global_lat = np.array([])
    global_lon = np.array([])
    for row in files:
        row_elev = np.array([])
        row_lat = np.array([])
        row_lon = np.array([])
        for (lat,lon) in row:
            elev_map = DEM.DEM(lat,lon)

            if row_elev.shape == (0,):
                row_elev = elev_map.elevations
                row_lat = elev_map.latlon[1]
                row_lon = elev_map.latlon[0]

            else:
                row_elev = np.append(row_elev, elev_map.elevations, axis=1)
                row_lat = np.append(row_lat, elev_map.latlon[1], axis=1)
                row_lon = np.append(row_lon, elev_map.latlon[0], axis=1)

        if global_elev.shape==(0,):
            global_elev = row_elev
            global_lat = row_lat
            global_lon = row_lon

        else:
            global_elev = np.append(global_elev, row_elev, axis=0)
            global_lat = np.append(global_lat, row_lat, axis=0)
            global_lon = np.append(global_lon, row_lon, axis=0)

    print global_elev.shape
    while global_elev.shape[0]>_res_limit:
        print("Downsampling axis=0")
        global_elev = global_elev[::2]
        global_lat = global_lat[::2]
        global_lon = global_lon[::2]

    while global_elev.shape[1]>_res_limit:
        print("Downsampling axis=1")
        global_elev = global_elev[:, ::2]
        global_lat = global_lat[:, ::2]
        global_lon = global_lon[:, ::2]

    latlon = [global_lon, global_lat]
    elev_map.longitudes = global_lon[0,:]
    elev_map.latitudes = global_lat[:,0]

    elev_map.elevations = global_elev
    elev_map.latlon = latlon

    return elev_map
