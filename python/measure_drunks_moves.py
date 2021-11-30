# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:11:59 2021

@author: Tom Cunningham
"""

import drunk_functions
import matplotlib
import timeit

# Set start time to time programme
start_time = timeit.default_timer()

# Set maximum number of moves (if this is too low it will affect results)
max_moves = 50000000000

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
        
        for i in range(max_moves):
    
            for drunk in drunks:
                drunk.move()
                drunk.sober_up()
            
            if all([drunk.is_home for drunk in drunks]):
                moves.append(i)
                break

    drunk_level_moves.append(moves)

# Plot results as boxplots
matplotlib.pyplot.boxplot(drunk_level_moves, positions = drunk_levels)

# Set end time
end_time = timeit.default_timer()
time_taken = end_time - start_time

# Calculate time taken to run
print("Time taken: " + str(time_taken))