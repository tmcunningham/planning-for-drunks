# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:23:02 2021

@author: c27028tc
"""
import random

class Drunk():
    def __init__(self, id, x, y, town, building_coords, drunk_level):
        self.id = id
        self._x = x
        self._y = y
        self.town = town
        self.building_coords = building_coords
        self.is_home = False
        self.home_coords = building_coords[id]
        self.other_building_coords = set([x for l in self.building_coords.values()\
                                          for x in l if x not in self.home_coords])
        self.history = []
        self.max_drunk_level = drunk_level
        self.drunk_level = drunk_level
        self.speed = 1
        
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
            
            
            """
            if self.drunk_level > 0:
                random_num = random.random()
                        
                if random_num < 0.25:
                    self.y = (self.y + self.speed) % len(self.town)
                elif random_num < 0.5:
                    self.y = (self.y - self.speed) % len(self.town)
                elif random_num < 0.75:
                    self.x = (self.x + self.speed) % len(self.town[0])
                else:
                    self.x = (self.x - self.speed) % len(self.town[0])
            
            else:
                    # If drunk level == 0 set closest home coords
                    closest_home_y = min([t[1] for t in self.home_coords],
                                         key = lambda y: abs(y - self.y))   
                    closest_home_x = min([t[0] for t in self.home_coords],
                                         key = lambda x: abs(x - self.x))
                   
                    if  closest_home_y > self.y:
                        self.y = (self.y + self.speed) % len(self.town)
                    elif closest_home_y < self.y:
                        self.y = (self.y - self.speed) % len(self.town)
                    elif closest_home_x > self.x:
                        self.x = (self.x + self.speed) % len(self.town[0])
                    else:
                        self.x = (self.x - self.speed) % len(self.town[0])
            
            if 
        
            
            """
            if self.drunk_level > 0:
                # Call random once so using the same random number - noticed a bug
                random_num = random.random()
                
                if random_num < 0.25:
                    new_y = (self.y + self.speed) % len(self.town)
                    new_x = self.x
                elif random_num < 0.5:
                    new_y = (self.y - self.speed) % len(self.town)
                    new_x = self.x
                elif random_num < 0.75:
                    new_x = (self.x + self.speed) % len(self.town[0])
                    new_y = self.y
                else:
                    new_x = (self.x - self.speed) % len(self.town[0])                
                    new_y = self.y
                
                
                
            else:
            
                # If drunk level == 0 set closest home coords
                closest_home_y = min([t[1] for t in self.home_coords],
                                     key = lambda y: abs(y - self.y))   
                closest_home_x = min([t[0] for t in self.home_coords],
                                     key = lambda x: abs(x - self.x))
                
                #rand_home_coord = random.choice(self.home_coords)
                if  closest_home_y > self.y:
                   new_y = (self.y + self.speed) % len(self.town)
                   new_x = self.x
                elif closest_home_y < self.y:
                    new_y = (self.y - self.speed) % len(self.town)
                    new_x = self.x
                if closest_home_x > self.x:
                    new_x = (self.x + self.speed) % len(self.town[0])
                    new_y = self.y
                else:
                    new_x = (self.x - self.speed) % len(self.town[0])
                    new_y = self.y
            
            
            # Update x and y if they are not building co-ordinates
            # If they are, start to go around the building
                        
            if (new_x, new_y) not in self.other_building_coords:
                (self.x, self.y) = new_x, new_y
            elif (new_x, self.y) in self.other_building_coords:
                (self.x, self.y) = (self.x, (self.y + self.speed) % len(self.town))
            elif (self.x, new_y) in self.other_building_coords:
                (self.x, self.y) = (self.x + self.speed % len(self.town[0]), self.y)
                
                
                
            
            
            
            # Add to environment to show route taken
            # If drunk doesn't move, will still add
            self.town[self.y][self.x] += 3
            
            # If reached one of home coordinates, set to be at home
            if (self.x, self.y) in self.home_coords:
                self.is_home = True
      
    def sober_up(self):
        if ((self.x, self.y) in self.history) and (self.drunk_level > 0):
            self.drunk_level -= 1
            if self.drunk_level <= self.max_drunk_level / 2:
                self.speed = 2
            elif self.drunk_level <= self.max_drunk_level/ 4:
                self.speed = 3
                
        self.history.append((self.x, self.y))
            
            
        """
        # Stop drunks walking over buildings
        if (new_x, new_y) not in \
        [x for l in self.building_coords.values() for x in l]:
            self.x, self.y = new_x, new_y
        
        self.town[self.y][self.x] += 1
        """

