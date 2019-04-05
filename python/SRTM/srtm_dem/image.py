"""

Script image.py plots a composite image of multiple DEM files on one image

"""

import os

import numpy as np
from matplotlib import pyplot as plt

import DEM
import filemanager
import stitch

def multi_plot(lat_range, lon_range, mode = "elevation"):
    """multi_plot plots elevations for multiple files"""
    lat_range_orig = np.array(lat_range)
    lon_range_orig = np.array(lon_range)
    lat_range = [np.floor(lat_range[0]), np.ceil(lat_range[1])]
    lon_range = [np.floor(lon_range[0]), np.ceil(lon_range[1])]
    print(lat_range)
    print(lon_range)
    lat_str = []
    for lat in (lat_range[0], lat_range[-1]):
        lat_str.append("N%s"%int(np.floor(lat)) if lat>=0 else\
                "S%s"%int(abs(np.floor(lat))))
    lon_str = []
    for lon in (lon_range[0], lon_range[-1]):
        lon_str.append("E%s"%int(np.floor(lon)) if lon>=0 else\
                "W%.3d"%int(abs(np.floor(lon))))
    lat_str = '_'.join(lat_str)
    lon_str = '_'.join(lon_str)
    coords = stitch.fetch_coords(lat_range, lon_range)
    print(coords)
    dem = stitch.stitch(coords)
    print(dem.elevations.shape)
    # Plotting commands
    fig, ax = plt.subplots()
    elev = dem.elevations[::-1].astype(int)
    elev[elev==DEM._fill] = 1.
    if mode == "elevation":
        eplt = ax.pcolormesh(dem.latlon[0], dem.latlon[1][::-1], elev, cmap = 'gist_earth')
        cbar = fig.colorbar(eplt)
        cbar.set_label("Elevation (m)")
        plot_title = "{}_x_{}_elev.png".format(lat_str, lon_str)

    elif mode == "relief":
        x, y = np.gradient(elev)
        slope = np.pi/2. - np.arctan(np.sqrt(x*x + y*y))
        aspect = np.arctan2(-x, y)
        altitude = np.pi / 6.
        azimuth = np.pi/2.

        shaded = np.sin(altitude)*np.sin(slope) + np.cos(altitude)*np.cos(slope)\
                    *np.cos((azimuth - np.pi/2.) - aspect)

        extent = (lon_range[0], lon_range[-1] , lat_range[-1], lat_range[0])
        eplt = ax.imshow(shaded, extent = extent, cmap="Greys", alpha = 0.85,
                    interpolation = "none", origin="upper", vmin=-1.2, vmax=1.2)
        cplt = ax.imshow(elev, extent = extent, cmap = "gist_earth",
                        alpha = 0.2, origin = "upper", interpolation="none")

        print(lon_range_orig)
        print(lat_range_orig)
        plot_title = "{}_x_{}_relief.png".format(lat_str, lon_str)

    else:
        raise TypeError("Invalid value for 'mode'")
    ax.set_xlim(*lon_range_orig)
    ax.set_ylim(*lat_range_orig)
    ax.set_title(os.path.splitext(plot_title)[0])
    ax.set_xlabel("Longitude ($^{\circ}$E)")
    ax.set_ylabel("Latitude ($^{\circ}$N)")
    ax.grid()

    img_path = os.path.join("../Images", plot_title)
    fig.savefig(img_path, dpi=600)
    print("Image saved as %s" % img_path)
    return (fig, ax)

if __name__ == "__main__":
    # multi_plot((42, 46), (-81, -77), mode="relief")
    multi_plot((43.25, 43.5), (-80.1, -79.9), mode = 'relief')
