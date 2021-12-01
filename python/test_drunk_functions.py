# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:27:15 2021

@author: Tom Cunningham

This module tests the functions in drunk_fucntions using the unittest module.

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
            result = drunk_functions.catch_input(2, int)
            self.assertEqual(result, 1)
    
    def test_int_undesired(self):
        """
        Test that when int is inputted but str is required, output is string.
        """
        with unittest.mock.patch('builtins.input', return_value = 1):
            result = drunk_functions.catch_input("a", str)
            self.assertEqual(result, "1")

