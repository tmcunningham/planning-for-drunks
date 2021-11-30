# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:19:45 2021

@author: Tom Cunningham
"""

import csv
import matplotlib.animation
import matplotlib.pyplot
import drunk_functions
import timeit

# Define maximum number of iterations
num_of_moves = 5000

# Define the limits for how drunk the drunks are
# A random number will be chosen between these two values for each drunk
drunk_level_lower = 20
drunk_level_higher = 20

# Set start time to time programme
start_time = timeit.default_timer

# Import town data
town = drunk_functions.import_town("drunk.plan")

# Check data has correct dimensions
#len(town)
#len(town[0])

# Plot data        
# matplotlib.pyplot.imshow(town)

"""
# Make pub clearer for plotting
for i in range(len(town)):
    for j in range(len(town[i])):
        if town[i][j] == 1:
            town[i][j] = -50
"""

# Set building coordinates
building_coords = drunk_functions.get_building_coords(town)

# Set front door coordinates
front_door_coords = drunk_functions.get_pub_front_door(building_coords)

# Set back door coordinates
back_door_coords = drunk_functions.get_pub_back_door(building_coords)

# Create drunks
drunks = drunk_functions.create_drunks(town, building_coords,
                                       front_door_coords, back_door_coords,
                                       drunk_level_lower, 
                                       drunk_level_higher)

# Create figure
fig = matplotlib.pyplot.figure(figsize = (7,7), frameon = False)
        
# Create animation
animation = matplotlib.animation.FuncAnimation(fig, drunk_functions.update, 
                                               fargs = (drunks, fig, town,),
                                               interval=1, 
                                               repeat = False, 
                                               frames = drunk_functions.gen_function(num_of_moves, drunks))
matplotlib.pyplot.show()


# Write town data to file
with open("town_out.txt", "w", newline = "") as f2:
            writer = csv.writer(f2, delimiter = ",")
            for row in town:
                writer.writerow(row)


