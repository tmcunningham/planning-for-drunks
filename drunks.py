# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:23:02 2021

@author: c27028tc
"""
import random

class Drunk():
    def __init__(self, id, x, y, town):
        self.id = id
        self._x = x
        self._y = y
        
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
        if random.random() < 0.25:
            self.y += 1
        elif random.random < 0.5:
            self.y -= 1
        elif random.random < 0.75:
            self.x += 1
        else:
            self.x -=1
        
        self.town[self.y][self.x] += 1

