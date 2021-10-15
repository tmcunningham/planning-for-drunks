# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:19:45 2021

@author: c27028tc
"""

import csv
import matplotlib.animation
import matplotlib.pyplot
import operator
import drunksframework
import random

# Define maximum number of iterations
num_of_moves = 5000
# Define the limits for how drunk the drunks are - a random number will be
# chosen between these two values for each drunk
drunk_level_lower = 300
drunk_level_higher = 2000

# Create figure
fig = matplotlib.pyplot.figure(figsize = (10,10), frameon = False)

# Read in town data and format it as a list of lists
with open("drunk.plan", newline = "") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    town = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        town.append(rowlist)

# Check data has correct dimensions
#len(town)
#len(town[0])

# Plot data        
# matplotlib.pyplot.imshow(town)

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

# Make pub clearer for plotting
for i in range(len(town)):
    for j in range(len(town[i])):
        if town[i][j] == 1:
            town[i][j] = 300            

# Set front door coords to be outside bottom left corner of pub
front_door_y = min(building_coords["pub"], key = operator.itemgetter(1))[1] - 1
front_door_x = min(building_coords["pub"], key = operator.itemgetter(0))[0] - 1

front_door_coords = (front_door_x, front_door_y)

# Set back door coords to be outside top right corner of pub
back_door_y = max(building_coords["pub"], key = operator.itemgetter(1))[1] + 1
back_door_x = max(building_coords["pub"], key = operator.itemgetter(0))[0] + 1

back_door_coords = (back_door_x, back_door_y)

# Create empty list for drunks         
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

# Create carry on variable for stopping condition of animation
carry_on = True    

def update(frame_number):
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

# Define generator function that stops if carry_on False or if num_of_moves met
def gen_function():
    global carry_on
    i = 0
    while (i < num_of_moves) & (carry_on):
        yield i
        i += 1
    else:
        carry_on = False
        print(str(sum([d.is_home for d in drunks])), "drunks got home.")
        

# Create animation
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, 
                                               repeat = False, 
                                               frames = gen_function())
matplotlib.pyplot.show()      



