# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:19:45 2021

@author: c27028tc
"""

import csv
import matplotlib
import operator
import drunksframework

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
matplotlib.pyplot.imshow(town)

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
                          

pub_door_y = min(building_coords["pub"], key = operator.itemgetter(1))[1]
pub_door_x = min(building_coords["pub"], key = operator.itemgetter(0))[0]

pub_door_coords = (pub_door_x, pub_door_y)

if pub_door_coords not in building_coords["pub"]:
    print("Pub door could not be found")
              
drunks = []

for id in range(10, 260, 10):
    drunks.append(drunksframework.Drunk(id = id, 
                                        x = pub_door_x, 
                                        y = pub_door_y,
                                        town = town,
                                        building_coords = building_coords))

for i in range(10000):
    for j in range(len(drunks)):
        drunks[j].move()
        
    if all([drunk.is_home for drunk in drunks]):
        print("All drunks home in " + str(i) + " moves.")
        break
    
print(str(sum([drunk.is_home for drunk in drunks])) + " drunks got home.")

        #print(drunks[j].x)
        
matplotlib.pyplot.imshow(town)
for j in range(len(drunks)):
    matplotlib.pyplot.scatter(drunks[j].x, drunks[j].y)
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


