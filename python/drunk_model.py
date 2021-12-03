# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:19:45 2021

@author: Tom Cunningham

This module runs an animation of drunks leaving a pub and moving around the
town until they reach their home. It allows users to set a maximum number of 
iterations of the model to run and limits for how drunk the drunks are. As well
as an animation, the module produces a text output of the raster data of the
town after the drunks have finished moving.

"""

import matplotlib.animation
import matplotlib.pyplot
import drunk_functions
import timeit
import sys
  
# Set maximum number of iterations
try:
    num_of_moves = int(sys.argv[1]) 
except:
    num_of_moves = drunk_functions.catch_input(
        5000, int, "Please specify a max number of iterations: ",
        "Input not recognised as integer.",
        "Number of moves set to default of 5000.\n"
        )

# Set drunk_level_lower for drunks
# A random number will be chosen between lower and upper values for each drunk
try:
    drunk_level_lower = int(sys.argv[2]) 
except:
    drunk_level_lower = drunk_functions.catch_input(
        20, int, 
        "Please specify a lower limit for drunk level as an integer: ",
        "Input not recognised as integer.",
        "Lower drunk level set to default of 20.\n"
        )

# Set drunk_level_higher for drunks
try:
    drunk_level_higher = int(sys.argv[3]) 
except:
    drunk_level_higher = drunk_functions.catch_input(
        drunk_level_lower + 50, int, 
        "Please specify an upper limit for drunk level as an integer: ",
        "Input not recognised as integer.",
        str("Upper drunk level set to default of ") +
            str(drunk_level_lower + 200)
        )

# Use smallest value as lower level and largest as upper
drunk_level_lower = min(drunk_level_lower, drunk_level_higher)
drunk_level_higher = max(drunk_level_lower, drunk_level_higher)

print("Number of iterations: " + str(num_of_moves),
      "\nLower drunk level: " + str(drunk_level_lower),
      "\nUpper drunk level: " + str(drunk_level_higher))

# Set start time to time programme
start_time = timeit.default_timer()

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
animation = matplotlib.animation.FuncAnimation(
    fig, 
    drunk_functions.update, 
    fargs = (drunks, fig, town, drunk_level_lower, drunk_level_higher,),
    interval=1,
    repeat = False, 
    frames = drunk_functions.gen_function(num_of_moves, drunks, town)
    )

matplotlib.pyplot.show()

# Stop timer and print time taken
end_time = timeit.default_timer()
print("Time taken: " + str(end_time - start_time))


