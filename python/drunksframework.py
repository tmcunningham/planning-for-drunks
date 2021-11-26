# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:23:02 2021

@author: Tom Cunningham
"""
import random

class Drunk():
    """
    Defines an instance of a single drunk person.
    
    Properties
    ----------
    id : int
        the number of the drunk's house
    x : int 
        the drunk's current x co-ordinate
    y : int
        the drunk's current y co-ordinate
    town : list
        raster data of town
    building_coords : dict 
        all of the town's building's co-ordinates as values, with names as keys
    is_home : bool
        indicates whether a drunk is at their home
    home_coords : list
        all coordinates of a drunk's home
    front_door : tuple
        co-ordinate of drunk's front door - closest home_coord to start point
    other_building_coords : set
        co-ordinates of buildings that are not drunk's home
    history : list
        all co-ordinates drunk has previously visited
    drunk_level : int
        number indicating how drunk the drunk currently is
    start_level : int
        the drunk's starting drunk_level
    speed : int
        how fast the drunk currently moves (i.e. how many spaces)
               
    Methods
    -------
    move()
        Moves the drunk while avoiding buildings. Either:
            moves randomly up, down, left or right (if still drunk) 
            or towards home if drunk_level is 0 (i.e. drunk has sobered up)
    
    sober_up()
        Decreases drunk level by one. Increases drunk's speed if level drops 
        below half or below a quarter of start level. Adds current position to
        history.
    """
    
    def __init__(self, id, x, y, town, building_coords, drunk_level):
        """
        Parameters
        ----------
        id : int
            the number of the drunk's house
        x : int 
            the drunk's current x co-ordinate
        y : int
            the drunk's current y co-ordinate
        town : list
            raster data of town
        building_coords : dict 
            all of the town's building's co-ordinates as values, with names as 
            keys
        drunk_level : int
            number indicating how drunk the drunk currently is
        """
        self.id = id
        self._x = x
        self._y = y
        self.town = town
        self.building_coords = building_coords
        self.is_home = False
        self.home_coords = building_coords[id]
        self.front_door = min([t for t in self.home_coords],
                              key = lambda a: ((a[1]-self.y)**2 + \
                                               (a[0]-self.x)**2)**0.5)
        self.other_building_coords = set([x for l in \
                                          self.building_coords.values() \
                                          for x in l if x not in \
                                          self.home_coords])
        self.history = []
        self.drunk_level = drunk_level
        self.start_drunk_level = drunk_level
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
    
    # Move up down left or right (not diagonally)
    def move(self):
        """
        Move the drunk according to whether or not their drunk level is 0.
        
        If drunk level is > 0 (i.e. still drunk) move drunk randomly up, down,
        left or right. If drunk level is 0 (i.e. relatively sober) move drunk
        towards their front door, choosing randomly whether to alter x or y
        co-ordinate. In both cases, only set new x or y if it is not in a
        non-home building. Otherwise, alter other co-ordinate.
        """
        # If not already at home, move up down left or right
        if not self.is_home:
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
                # If drunk_level == 0, move drunk towards home
                # Randomise whether to change x or y coord first
                if random.random() < 0.5:
                    if  self.front_door[1] > self.y:
                        new_y = (self.y + self.speed) % len(self.town)
                        new_x = self.x
                    elif self.front_door[1] < self.y:
                        new_y = (self.y - self.speed) % len(self.town)
                        new_x = self.x
                    elif self.front_door[0] > self.x:
                        new_x = (self.x + self.speed) % len(self.town[0])
                        new_y = self.y
                    else:
                        new_x = (self.x - self.speed) % len(self.town[0])
                        new_y = self.y
                        
                else:
                    if self.front_door[0] > self.x:
                        new_x = (self.x + self.speed) % len(self.town[0])
                        new_y = self.y 
                    elif self.front_door[0] < self.x:
                        new_x = (self.x - self.speed) % len(self.town[0])
                        new_y = self.y 
                    elif self.front_door[1] > self.y:
                        new_y = (self.y + self.speed) % len(self.town)
                        new_x = self.x
                    else:
                        new_y = (self.y - self.speed) % len(self.town)
                        new_x = self.x
            
            
            # Update x and y if they are not building co-ordinates
            # If they are, start to go around the building
                        
            
            if (new_x, new_y) not in self.other_building_coords:
                (self.x, self.y) = new_x, new_y
            elif (new_x, self.y) in self.other_building_coords:
                if random.random() > 0.5:
                    self.y = (self.y + self.speed) % len(self.town)
                else:
                    self.y = (self.y - self.speed) % len(self.town)
            elif (self.x, new_y) in self.other_building_coords:
                if random.random() > 0.5:
                    self.x = (self.x + self.speed) % len(self.town)
                else: 
                    self.x = (self.x - self.speed) % len(self.town)
            
            if (self.x, self.y) in self.other_building_coords:
                print(str(self.id), "in a building")
            
            # Add to environment to show route taken
            # If drunk doesn't move, will still add
            self.town[self.y][self.x] += 3
            
            # If reached one of home coordinates, set to be at home
            if (self.x, self.y) in self.home_coords:
                self.is_home = True
      
    def sober_up(self):
        """
        Decrease drunk level of drunk ond alters speed. Add x and y to history.
        
        Decrease
        """
        if ((self.x, self.y) in self.history) and (self.drunk_level > 0):
            self.drunk_level -= 1
            if self.drunk_level <= self.start_drunk_level / 2:
                self.speed = 3
            elif self.drunk_level <= self.start_drunk_level/ 4:
                self.speed = 5
        
        if not self.is_home: 
            self.history.append((self.x, self.y))
            
            
        """
        # Stop drunks walking over buildings
        if (new_x, new_y) not in \
        [x for l in self.building_coords.values() for x in l]:
            self.x, self.y = new_x, new_y
        
        self.town[self.y][self.x] += 1
        """

