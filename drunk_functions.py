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

def import_town():
    # Read in town data and format it as a list of lists
    with open("drunk.plan", newline = "") as f:
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
    
def set_building_coords(town):
    #Create empty dictionary to collect building co-ordinates
    building_coords = {}
    
    # Create list of co-ordinates for each building in the town
    # Dictionary key is either "pub" or building number and value is list of coords
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
def set_pub_front_door(building_coords):
    # Set front door coords to be outside bottom left corner of pub
    front_door_y = min(building_coords["pub"], key = operator.itemgetter(1))[1] - 1
    front_door_x = min(building_coords["pub"], key = operator.itemgetter(0))[0] - 1
    
    front_door_coords = (front_door_x, front_door_y)
    
    return front_door_coords

def set_pub_back_door(building_coords):
    # Set back door coords to be outside top right corner of pub
    back_door_y = max(building_coords["pub"], key = operator.itemgetter(1))[1] + 1
    back_door_x = max(building_coords["pub"], key = operator.itemgetter(0))[0] + 1
    
    back_door_coords = (back_door_x, back_door_y)
    
    return back_door_coords

def create_drunks(town, building_coords, front_door_coords, back_door_coords,
                  drunk_level_lower, drunk_level_higher):
    drunks = []   
    
    # Create drunks - start at front or back door of pub at random
    for id in range(10, 260, 10):
        pub_door_coords = random.choice([front_door_coords, back_door_coords])
        
        drunks.append(drunksframework.Drunk(id = id, 
                                            #x = building_coords[20][0][0],                                        
                                            #y = building_coords[20][0][1],
                                            x = pub_door_coords[0],
                                            y = pub_door_coords[1],
                                            town = town,
                                            building_coords = building_coords,
                                            drunk_level = random.randint(drunk_level_lower,
                                                                         drunk_level_higher)))
        
    return drunks

def update(frame_number, drunks, fig, town):
    global carry_on
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
    
    
    # Print how long it took to get all drunks home
    if all([drunk.is_home for drunk in drunks]):
        carry_on = False
        print("All drunks home in " + str(frame_number) + " moves.")

# Define gen function that stops if all drunks home or if num_of_moves met
def gen_function(num_of_moves, drunks):
    i = 0
    while (i < num_of_moves) & (any([not drunk.is_home for drunk in drunks])):
        yield i
        i += 1
    else:
        print(str(sum([d.is_home for d in drunks])), "drunks got home.")
        
        


