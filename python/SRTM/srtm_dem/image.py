"""

Script image.py plots a composite image of multiple DEM files on one image

"""

import os

import numpy as np
from matplotlib import pyplot as plt

import DEM

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
            print (lat, lon)
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

    latlon = [global_lon, global_lat]

    elev_map.elevations = global_elev
    elev_map.latlon = latlon
    elev_map.longitudes = latlon[0][0,:]
    elev_map.latitudes = latlon[1][:,0]

    return elev_map

def plot(dem, title=None, save_as=None):
    fig, ax = plt.subplots()
    elev = np.ma.masked_equal(dem.elevations[::-1].astype(int), DEM._fill)
    color_plot = ax.pcolormesh(dem.latlon[0], dem.latlon[1][::-1], elev)

    ax.set_xlim(dem.longitudes[0], dem.longitudes[-1])
    ax.set_ylim(dem.latitudes[-1], dem.latitudes[0])

    cbar = fig.colorbar(color_plot)

    cbar.set_label("Elevation (m)")


    if title:
        ax.set_title(title)
    else:
        def_title = os.path.splitext(dem.srtm_dem)[0]
        ax.set_title(def_title)

    ax.set_xlabel("Longitude ($^{\circ}$E)")
    ax.set_ylabel("Latitude ($^{\circ}$N)")

    ax.grid()
    if save_as:
        save_path = save_as
    else:
        save_path = '../Images/{}.png'.format(dem.srtm_dem)
    fig.savefig(save_path, dpi=600)

def multi_plot(lat_range, lon_range):

    lat_str = []
    for lat in (lat_range[0], lat_range[-1]):
        lat_str.append("N%s"%int(np.floor(lat)) if lat>=0 else "S%s"%int(abs(np.floor(lat))))

    lon_str = []
    for lon in (lon_range[0], lon_range[-1]):
        lon_str.append("E%s"%int(np.floor(lon)) if lon>=0 else "W%.3d"%int(abs(np.floor(lon))))

    lat_str = '_'.join(lat_str)
    lon_str = '_'.join(lon_str)

    plot_title = "{}_x_{}.png".format(lat_str, lon_str)
    img_path = os.path.join("../Images", plot_title)

    coords = fetch_coords(lat_range, lon_range)

    dem = stitch(coords)

    plot(dem, title = os.path.splitext(plot_title)[0], save_as = img_path)

if __name__ == "__main__":
    multi_plot((42, 45), (-81, -78))
