"""This function map the data we have received from
    read_neighbourhoods.py and exports the
    outputted map to PDF."""

#Let's importy numpy and various toold from cartopy and matplotlib.
import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np

#Let's import our functions from the last file.
from read_neighbourhoods import load_data, break_data

def plot_neighbourhoods(x_coords, y_coords):
    """This function plots the data onto a map"""
    #Sets the figure size
    plt.figure(figsize=(9, 11))
    #Takes data from Open Street Map
    tiler = OSM()
    #Plots axes
    ax = plt.axes(projection=ccrs.OSGB(approx=False))
    #Adds a background image from the Open Street Maps tiler
    ax.add_image(tiler, 10)
    ax.set_extent((300000, 342000, 655000, 680000),crs=ccrs.OSGB(approx=False))

    #This says that there are as many neighbourhoods as the list of xcoordinates is long.
    #This will make it easier to format the map.
    number_of_neighbourhoods = len(x_coords)
    #This then comes up with a number of unique coloiurs;
    neighbourhood_colours = cm.get_cmap("tab20", number_of_neighbourhoods)

    #This distributes the random colours randomly throughout the map
    colours = np.random.permutation(np.linspace(0,1, number_of_neighbourhoods))
    handles = []

    #This assigns each neighbourhood a numerical value so we can assign a colour to each.
    for i, neighbourhood in enumerate(x_coords):
        x_ordinates = x_coords[neighbourhood]
        y_ordinates = y_coords[neighbourhood]

        #This makes each neighbourhood polyogn a colour
        color = neighbourhood_colours(colours[i])

        #This deals with the appearance of each polygon.
        polygon = ax.fill(x_ordinates, y_ordinates, color=color, alpha=0.5, label=neighbourhood)
        ax.plot(x_ordinates, y_ordinates, linestyle="-", color='black')

        handles.append(polygon[0])

    #Adds a legend
    plt.legend(handles=handles, labels=x_coords.keys(), loc="upper left",
                bbox_to_anchor=(0, -0.1, 0.1, 0.1),
                ncol=6, title="Legend", frameon=False, fontsize='x-small')
    plt.subplots_adjust(bottom=0.3)
    #Adds a title
    plt.title('Neighbourhoods in Edinburgh', fontsize=20)
    #Congratulations!  It's the bit we've all been waiting for...
    #...This function plots the map!!!
    plt.savefig("Neighbourhoods in Edinburgh.pdf", bbox_inches="tight")
    plt.show(block=True)#imports the cartopy, matplotlib and numpy libraries.

if __name__ == '__main__':
    file_name = "task_2_data/natural_neighbourhoods.dat"
    data = load_data(file_name)
    x_coords, y_coords = break_data(data)
    plot_neighbourhoods(x_coords, y_coords)
