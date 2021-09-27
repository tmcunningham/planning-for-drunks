# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:19:45 2021

@author: c27028tc
"""

import csv
import matplotlib

with open("drunk.plan", newline = "") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    data = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        data.append(rowlist)

# Check data has correct dimensions
#len(data)
#len(data[0])

# Plot data        
matplotlib.pyplot.imshow(data)

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
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == n:
                building_coords[building_name].append((x, y))
                



"""
# Plot the pub to verify it is larger than other buildings
data2 = data

for i in range(len(data2)):
    for j in range(len(data2[i])):
        if data[i][j] == 1:
            data[i][j] = 200
        else:
            data[i][j] = 0
        
matplotlib.pyplot.imshow(data2)
"""


