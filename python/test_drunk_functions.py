# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:27:15 2021

@author: Tom Cunningham

This module tests the functions in drunk_functions using the unittest module.

"""

import unittest
import unittest.mock
import drunk_functions

class TestCatchInput(unittest.TestCase):
    def test_int_desired(self):
        """
        Test that when int is desired and inputted it is returned.
        """
        with unittest.mock.patch('builtins.input', return_value = 1):
            output = drunk_functions.catch_input(2, int)
            self.assertEqual(output, 1)
    
    def test_int_undesired(self):
        """
        Test that when int is inputted but str is required, output is string.
        """
        with unittest.mock.patch('builtins.input', return_value = 1):
            output = drunk_functions.catch_input("a", str)
            self.assertEqual(output, "1")
            
    def test_default(self):
        """
        Test that when input can't be parsed as desired type, default is used.
        """
        with unittest.mock.patch('builtins.input', return_value = "a"):
            output = drunk_functions.catch_input(1, int)
            self.assertEqual(output, 1)
            
class TestImportTown(unittest.TestCase):
    def test_dimensions(self):
        """
        Test importing drunk.plan gives a list of the correct dimensions.
        """
        output = drunk_functions.import_town("drunk.plan")
        self.assertEqual(len(output), 300)
        self.assertEqual(len(output[0]), 300)
        
class TestGetBuildingCoords(unittest.TestCase):
    def test_len(self):
        """
        Test getting building coords gives a dictionary of correct length.
        """
        output = drunk_functions.get_building_coords(
            drunk_functions.import_town("drunk.plan")            
            )
        self.assertIsInstance(output, dict)
        self.assertEqual(len(output), 26)
        
    def test_keys(self):
        """
        Test keys of returned dictionary contian the house numbers and pub.
        """
        output = drunk_functions.get_building_coords(
            drunk_functions.import_town("drunk.plan")            
            )
        self.assertTrue(set(range(10, 260, 10)).issubset(set(output.keys())))
        self.assertIn("pub", set(output.keys()))