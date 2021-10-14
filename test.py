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

num_of_moves = 50000
drunk_level = 1500

fig = matplotlib.pyplot.figure(figsize = (7,7), frameon = False)
#fig.add_axes([0, 0, 1, 1])
#fig.axes.get_xaxis().set_visible(False)
#fig.axes.get_yaxis().set_visible(False)

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

# Set front door coords to be bottom left corner of pub
front_door_y = min(building_coords["pub"], key = operator.itemgetter(1))[1] - 1
front_door_x = min(building_coords["pub"], key = operator.itemgetter(0))[0] - 1

front_door_coords = (front_door_x, front_door_y)

# Set back door coords to be top right corner of pub
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
                                        drunk_level = drunk_level))

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
    # Plot drunks   
    matplotlib.pyplot.imshow(town)
    matplotlib.pyplot.xlim(0, len(town[0]))
    matplotlib.pyplot.ylim(0, len(town))
    matplotlib.pyplot.tick_params(left = False, right = False , 
                                  labelleft = False, labelbottom = False, 
                                  bottom = False)
    for drunk in drunks:
        matplotlib.pyplot.scatter(drunk.x, drunk.y)
        
    if all([drunk.is_home for drunk in drunks]):
        carry_on = False
        print("All drunks home in " + str(frame_number) + " moves.")


def gen_function():
    global carry_on
    i = 0
    while (i < num_of_moves) & (carry_on):
        yield i
        i += 1
    else:
        print(str(sum([drunk.is_home for drunk in drunks])) + " drunks got home.")

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, 
                                               repeat = False, 
                                               frames = gen_function())
matplotlib.pyplot.show()      

"""
# Plot the pub to verify it is larger than other buildings
town2 = town

for i in range(len(town2)):
    for j in range(len(town2[i])):
        if town2[i][j] == 1:
            town2[i][j] = 400
        
matplotlib.pyplot.imshow(town2)
"""


