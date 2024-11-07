---
TASK 2
.py file names: read_neighbourhoods.py, plot_neighbourhoods.py
about: read, format and map data from natural_neighbourhoods.dat

---

These files allow for the mapping of data from the natural_neighbourhoods.dat dataset.  Firstly, the dataset is loaded into the read_neighbourhoods file which will read the data and format it into a dictionary called edinburgh_neighbourhoods.  This produces a series of (x,y) coordinates which denote the boundaries of each neighbourhood in the city.  These (x,y) points are formatted into two lists of x and y values which can are suitable for mapping in Cartopy.  In the plot_neighbourhoods.py file, these x and y values are taken and mapped using cartopy.

The plot_neighbourhoods.py file will produce a map of Edinburgh.  It then exports this map as a PDF file to the ~/s2657606_tigis_coding_assignment/task_2 directory.  

The numpy, matplotlib and cartopy libraries are imported in the plot_neighbourhoods.py file.  

NOTE:  Please allow a few seconds for the map figure to load...it's on its way!

Happy coding!!!
