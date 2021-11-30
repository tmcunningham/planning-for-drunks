# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 01:24:10 2021

@author: Tom Cunningham
"""

import csv
import matplotlib.animation
import matplotlib.pyplot
import operator
import drunksframework
import random

def catch_input(default_value, desired_type, input_message = "Input: ", 
                failure_message = "Invalid input.", 
                default_message = "Default value used.", num_attempts = 3):
    """
    Function to better catch type errors in user input. If the input can be 
    parsed using desired_type, then this value is returned. Otherwise, the 
    user will be asked again a number of times (up to num_attempts) and if the 
    input still results as an error, then the default_value is returned.

    Parameters
    ----------
    default_value : str
        Value returned if all inputs fail. Must be able to be parsed by
        desired_type.
    desired_type : type
        Desired type of the input (e.g. str, int).
    input_message : str, optional
        Prompt to user for input. The default is "Input: ".
    failure_message : str, optional
        Message to print when input fails. The default is "Invalid input.".
    default_message : str, optional
        Message to print when default_value used. The default is "Default 
        value used.".
    num_attempts : int, optional
        Number of times to attempt to prompt for input. The default is 3.

    Returns
    -------
    type as specified by desired_type
        Value of input if successful, or default_value otherwise.

    """
    attempt = 0
    while attempt < num_attempts:
        try:
            return desired_type(input(input_message))
            break
        except:
            print(failure_message)
            attempt += 1
            continue
    else:
        print(default_message)
        return desired_type(default_value)

def import_town(data_file):
    """
    Reads town raster data from a CSV file.

    Parameters
    ----------
    data_file : str
        Name of CSV raster data file to use for the town.

    Returns
    -------
    town : list
        List (cols) of lists (rows) representing raster data of the town. 

    """
    # Read in town data and format it as a list of lists
    with open(data_file, newline = "") as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        town = []
        for row in reader:
            rowlist = []
            for value in row:
                rowlist.append(value)
            town.append(rowlist)
    
    return town
    
    # Check data has correct dimensions
    #len(town)
    #len(town[0])
    
    # Plot data        
    # matplotlib.pyplot.imshow(town)
    
def get_building_coords(town):
    """
    Generates a dictionary of all (x,y) co-ordinates that are within buildings
    in the town, where the keys are the buildings' numbers (or "pub" for the 
    pub) and the values are lists of co-ordinates associated with the building.
    Data must have 25 houses (numbered as multiples of 10 from 10 to 250) and
    1 pub.

    Parameters
    ----------
    town : list
        List (cols) of lists (rows) representing raster data of the town. 

    Returns
    -------
    building_coords : dict
        Keys are the buildings' numbers (or "pub" for the pub) and the values 
        are lists of all co-ordinates that are within the building.
        
    """
    #Create empty dictionary to collect building co-ordinates
    building_coords = {}
    
    # Create list of co-ordinates for each building in the town
    # Dictionary key is either "pub" or building number and value is list of 
    # coords
    for n in [1, *range(10, 260, 10)]:
        if n == 1:
            building_name = "pub"
        else:
            building_name = n
        building_coords[building_name] = []
        for y in range(len(town)):
            for x in range(len(town[y])):
                if town[y][x] == n:
                    building_coords[building_name].append((x, y))
                    
    return building_coords
    
    """
    # Make pub clearer for plotting
    for i in range(len(town)):
        for j in range(len(town[i])):
            if town[i][j] == 1:
                town[i][j] = -50
    """
def get_pub_front_door(building_coords):
    """
    Gets the co-ordinates just outside the front door (south-west corner) of
    the pub.

    Parameters
    ----------
    building_coords : dict
        Keys are the buildings' numbers (or "pub" for the pub) and the values 
        are lists of all co-ordinates that are within the building.

    Returns
    -------
    front_door_coords : tuple
        A length 2 tuple giving the (x,y) co-ordinates of the pub's front door.

    """
    # Set front door coords to be outside bottom left corner of pub
    front_door_y = min(building_coords["pub"], 
                       key = operator.itemgetter(1))[1] - 1
    front_door_x = min(building_coords["pub"], 
                       key = operator.itemgetter(0))[0] - 1
    
    front_door_coords = (front_door_x, front_door_y)
    
    return front_door_coords

def get_pub_back_door(building_coords):
    """
    Gets the co-ordinates just outside the back door (north-east corner) of
    the pub.

    Parameters
    ----------
    building_coords : dict
        Keys are the buildings' numbers (or "pub" for the pub) and the values 
        are lists of all co-ordinates that are within the building.

    Returns
    -------
    back_door_coords : tuple
        A length 2 tuple giving the (x,y) co-ordinates of the pub's back door.

    """
    # Set back door coords to be outside top right corner of pub
    back_door_y = max(building_coords["pub"], 
                      key = operator.itemgetter(1))[1] + 1
    back_door_x = max(building_coords["pub"], 
                      key = operator.itemgetter(0))[0] + 1
    
    back_door_coords = (back_door_x, back_door_y)
    
    return back_door_coords

def create_drunks(town, building_coords, front_door_coords, back_door_coords,
                  drunk_level_lower, drunk_level_higher):
    """
    Creates a list of 25 drunks using the drunk class framework, one for each
    house in the town data.

    Parameters
    ----------
    town : list
        List (cols) of lists (rows) representing raster data of the town. 
    building_coords : dict
        Keys are the buildings' numbers (or "pub" for the pub) and the values 
        are lists of all co-ordinates that are within the building.
    front_door_coords : tuple
        A length 2 tuple giving the (x,y) co-ordinates of the pub's front door.
    back_door_coords : tuple
        A length 2 tuple giving the (x,y) co-ordinates of the pub's back door.
    drunk_level_lower : int
        Lower limit for drunks' drunk level - will be chosen randomly between
        lower and higher level for each drunk.
    drunk_level_higher : int
        Upper limit for drunks' drunk level - will be chosen randomly between
        lower and higher level for each drunk.

    Returns
    -------
    drunks : list
        List of 25 drunks with ids that are multiples of 10 from 10 to 250.

    """
    drunks = []   
    
    # Create drunks - start at front or back door of pub at random
    for id in range(10, 260, 10):
        pub_door_coords = random.choice([front_door_coords, back_door_coords])
        
        drunks.append(
            drunksframework.Drunk(id = id, 
                                  #x = building_coords[20][0][0],                                        
                                  #y = building_coords[20][0][1],
                                  x = pub_door_coords[0],
                                  y = pub_door_coords[1],
                                  town = town,
                                  building_coords = building_coords,
                                  drunk_level = random.randint(
                                      drunk_level_lower,drunk_level_higher
                                      )
                                  )
            )
        
    return drunks

def update(frame_number, drunks, fig, town):
    """
    Uses the drunks' move and sober_up methods once per drunk in the drunks
    list and then plots the new state of the drunks and town.
    
    This function is used when creating an animation of the drunks' movement
    around the town.

    Parameters
    ----------
    frame_number : int
        Iteration of the model.
    drunks : list
        List of 25 instances of drunk class, with ids that are multiples of 10
        between 10 and 250.
    fig : matplotlib.figure.Figure
        Figure used for plotting.
    town : list
        List of lists representing raster data of the town.

    Returns
    -------
    None.

    """
    # global carry_on
    fig.clear()
    
    # Move drunks
    for drunk in drunks:
        #print(drunks[j].x)
        drunk.move()
        drunk.sober_up()
        #if (drunk.x, drunk.y) in building_coords["pub"]:
        #    print(drunk.id)
        #    break
    #print(drunks[5].x)
    #print(drunks[5].y)  
    
    
    # Plot town without ticks on axes
    matplotlib.pyplot.imshow(town)
    matplotlib.pyplot.xlim(0, len(town[0]))
    matplotlib.pyplot.ylim(0, len(town))
    matplotlib.pyplot.tick_params(left = False, right = False , 
                                  labelleft = False, labelbottom = False, 
                                  bottom = False)
    
    
    # Plot drunks
    for drunk in drunks:
        matplotlib.pyplot.scatter(drunk.x, drunk.y)
    
    """
    # Print how long it took to get all drunks home
    if all([drunk.is_home for drunk in drunks]):
        carry_on = False
        print("All drunks home in " + str(frame_number) + " moves.")
    """

# Define gen function that stops if all drunks home or if num_of_moves met
def gen_function(num_of_moves, drunks):
    """
    Generator function used in creating animation of drunks moving around town.
    Will continue to yield until either num_of_moves has been reached, or the
    carry_on variable is False (this will happen in the update function when
    all drunks get home).
    
    If all drunks get home or the maximum number of iterations is met, a
    message will be printed stating how many drunks got home and in how many 
    moves.

    Parameters
    ----------
    num_of_moves : int
        Maximum number of iterations for which the model will be run.
    drunks : list
        List of 25 instances of drunk class, with ids that are multiples of 10
        between 10 and 250.

    Yields
    ------
    i : int
        Iteration of the model

    """
    i = 0
    while (i < num_of_moves) & (any([not drunk.is_home for drunk in drunks])):
        yield i
        i += 1
    else:
        if all([drunk.is_home for drunk in drunks]):
            # carry_on = False
            print("All drunks home in " + str(i) + " moves.")
        else:
            print(str(sum([d.is_home for d in drunks])), " drunks home in " + 
                  str(i) + " moves.")
        
        


