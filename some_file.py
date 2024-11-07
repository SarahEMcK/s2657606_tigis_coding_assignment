"""This file uses the read_data and plotxy funtions to read and plot
    data from the plenty.data file"""

#Install numpy and matplotlib
import numpy as np
from matplotlib import pyplot

def read_data(file_name):
    """This function reads the data, later in the code, you will see
        that the specified dataset is called plenty.data in this
        case."""
    #Create empty lists for the x and y values
    x_coords = []
    y_coords = []
    #Open the file#
    with open(file_name, "r") as data:
        for line in data:
            #Split up the x and y Values...#
            #...and temporarily store them in place_holder#
            place_holder = line.split()
            x_coords.append(float(place_holder[0]))
            #As there is more than one y value for each x value...
            # ...the y values must be treated like an array.
            y_values = np.array([float(value) for value in place_holder[1:]])
            y_coords.append(y_values)
        #Return the (x,y) coordinate points#
    return x_coords, y_coords

#At this point in writing my code, I paused to have a mint humbug...
#...if you are reading, may I humbly suggest you do the same...!"""

def plotxy(x_axis, y_axis):
    """This function plots the data"""
    line_names = [f'y_axis{i+1}' for i in range (len(y_axis[0]))]
    #These lines of code deal with formatting the data
    pyplot.plot(x_axis, y_axis, label=line_names)
    pyplot.ylabel("Y COORDINATES", fontsize=12, fontstyle="italic")
    pyplot.xlabel("X COORDINATES", fontsize=12, fontstyle="italic")
    pyplot.title("DATA POINTS FROM PLENTY.DATA", fontsize=16)
    pyplot.grid(True)
    pyplot.legend(ncol=2)
    pyplot.show()

if __name__ == '__main__':
    xdata, ydata = read_data('task_1_data/plenty.data')
    plotxy(xdata, ydata)
