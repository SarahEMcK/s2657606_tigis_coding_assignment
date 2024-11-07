def load_data(file_name):
    """This function loads data from the file into an empty dictionary
        called edinburgh_neighbourhoods."""
    edinburgh_neighbourhoods = {}
    current_neighbourhood = None

    #Let's open and read the file_name and call it file.
    with open(file_name, "r") as file:
            #Let's get it to ignre the first three lines of the file...
            #Whilst they're important for telling whoever is reading the file what it is...
            #...we don't really need them here.
        for _ in range(3):
            next(file)
            
        for line in file:
            #Let's get rid of any trailing whitespace.
            line = line.strip()
            #If the line starts with something that's not a bracket, it must be a placename.#
            if line and not line.startswith("(") and not line.startswith("["):
                current_neighbourhood = line
                edinburgh_neighbourhoods[current_neighbourhood] = []
            #If the line starts with a bracket and we can see the name of a neighbourhood...
            #...then this is a point.
            elif line.startswith("(") and current_neighbourhood is not None:
                #breaks up the coordinates into their respective X and Y Values.
                coords = line.strip("()").split(', ')
                x, y = float(coords[0]), float(coords[1])
                #Joins the coordinates to the neighbourhood.
                edinburgh_neighbourhoods[current_neighbourhood].append((x,y))

            # If the line starts with [ it's going to need some formatting!
            elif line.startswith("[") and current_neighbourhood is not None:
                #This get's rid of the square brackets
                cleaned_line = line.strip("[]")
                #This splits any lists of points into individual points
                elements = cleaned_line.split("), (")
                for element in elements:
                    #This gets rid of the brackets.
                    element = element.strip("()")
                    #This gets rid of the commas between points.
                    numbers = element.split(", ")
                    #This tells us that the (x,y) points are floats and appends them to the list.
                    float_numbers = [float(num) for num in numbers]
                    edinburgh_neighbourhoods[current_neighbourhood].append(float_numbers)

    #Shows us what's in the dictionary#
    return edinburgh_neighbourhoods

#Now we have created a dictionary of every neighbourhood in Edinburgh...
#...from Abbeyhill to Wester Coates!

def break_data(edinburgh_neighbourhoods):
    """This function splits the tuples into (x,y) points"""
    #Sets up dictionary of x and y coordinates tied to the neighbourhood they belong to.
    x_coords = {}
    y_coords = {}
    #creates lists of all the x values and all the y values
    for neighbourhood, points in edinburgh_neighbourhoods.items():
        x_list = []
        y_list = []
        #loops through the points and appends the x and y values to their respective lists.
        for point in points:
            if isinstance(point, tuple):
                x_list.append(point[0])
                y_list.append(point[1])
            #This deals with the longer lists of points which were found in the data...
            #...and appends the x and y values to their respective lists.
            else:
                x_list.extend(point[0::2])
                y_list.extend(point[1::2])

        #Stores the x and y coordinates in their respective dictionaries.
        x_coords[neighbourhood] = x_list
        y_coords[neighbourhood] = y_list 
    #returns the lists of x and y coords.
    return x_coords, y_coords

if __name__ == '__main__':
    file_name = 'task_2_data/natural_neighbourhoods.dat'
    data = load_data(file_name)
    x_coords, y_coords = break_data(data) 
    print ("Well aren't you just awesome!  Congratulations, the function worked...you're ready to start mapping!")