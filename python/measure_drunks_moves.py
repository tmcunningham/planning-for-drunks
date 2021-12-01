# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:11:59 2021

@author: Tom Cunningham

This module uses the drunk_functions module to track how many moves it takes
all drunks to get home at a range of drunk levels. The module will produce a
boxplot of the results.

"""

import drunk_functions
import matplotlib
import timeit

# Set start time to time programme
start_time = timeit.default_timer()

# Import town data
town = drunk_functions.import_town("drunk.plan")

# Set building coordinates
building_coords = drunk_functions.get_building_coords(town)

# Set front door coordinates
front_door_coords = drunk_functions.get_pub_front_door(building_coords)

# Set back door coordinates
back_door_coords = drunk_functions.get_pub_back_door(building_coords)

# Set drunk levels to be tested
drunk_levels = [10, 20, 50, 100, 200]

# Set number of iterations to run model for each drunk_level
iterations = 1000
    
# Create empty list to store move counts
drunk_level_moves = []

# Loop over all drunk levels and run model set number of times and record how
# long it took for all drunks to get home
for drunk_level in drunk_levels:
    drunk_level_lower = drunk_level
    drunk_level_higher = drunk_level
    moves = []

    for i in range(iterations):
        drunks = drunk_functions.create_drunks(town, building_coords, 
                                               front_door_coords, back_door_coords,
                                               drunk_level_lower, 
                                               drunk_level_higher)
        j = 0
        while not all([drunk.is_home for drunk in drunks]):
            for drunk in drunks:
                drunk.move()
                drunk.sober_up()
            j += 1
        else:
            moves.append(j)
    
        print("Drunk level " + str(drunk_level) + ": " + str(i/(iterations-1)))
    
    drunk_level_moves.append(moves)

# Plot results as boxplots
matplotlib.pyplot.boxplot(drunk_level_moves, positions = drunk_levels)
matplotlib.pyplot.savefig("Number of moves boxplot.png")

# Set end time
end_time = timeit.default_timer()
time_taken = end_time - start_time

# Calculate time taken to run
print("Time taken: " + str(time_taken))