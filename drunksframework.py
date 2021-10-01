# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:23:02 2021

@author: c27028tc
"""
import random

class Drunk():
    def __init__(self, id, x, y, town, building_coords):
        self.id = id
        self._x = x
        self._y = y
        self.town = town
        self.building_coords = building_coords
        self.is_home = False
        self.home_coords = building_coords[id]
        
    def get_x(self):
        return self._x
    
    def set_x(self, value):
        self._x = value
        
    def get_y(self):
        return self._y
    
    def set_y(self, value):
        self._y = value
    
    x = property(get_x, set_x, "x property")
    y = property(get_y, set_y, "y property")
    
    # Move up down left or right (not diagonally) at random
    def move(self):
        # If not already at home, move up down left or right at random
        if not self.is_home:
            (new_x, new_y) = self.x, self.y
            
            
            # Call random once so using the same random number - noticed a bug
            random_num = random.random()
            
            if random_num < 0.25:
                new_y = (new_y + 1) % len(self.town)
            elif random_num < 0.5:
                new_y = (new_y - 1) % len(self.town)
            elif random_num < 0.75:
                new_x = (new_x + 1) % len(self.town[0])
            else:
                new_x = (new_x - 1) % len(self.town[0])
            
            # Update x and y if they are not building co-ordinates
            # This is currently really slowing everything down
            if (new_x, new_y) not in \
            [x for l in self.building_coords.values() for x in l]:
                (self.x, self.y) = new_x, new_y
            
            # Add one to environment to show route taken
            self.town[self.y][self.x] += 1
            
            # If reached one of home coordinates, set to be at home
            if (self.x, self.y) in self.home_coords:
                self.is_home = True
            
        """
        # Stop drunks walking over buildings
        if (new_x, new_y) not in \
        [x for l in self.building_coords.values() for x in l]:
            self.x, self.y = new_x, new_y
        
        self.town[self.y][self.x] += 1
        """

