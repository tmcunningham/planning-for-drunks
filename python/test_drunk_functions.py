# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:27:15 2021

@author: Tom Cunningham

This module tests the functions in drunk_functions and drunksframework using 
the unittest module.

"""

import unittest
import unittest.mock
import drunk_functions
import drunksframework
from io import StringIO

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
        Test that when input can't be parsed as desired type, default is used
        and printed message is as expected.
        """
        with unittest.mock.patch('sys.stdout', new = StringIO()) as mock_out:
            with unittest.mock.patch('builtins.input', return_value = "a"):
                output = drunk_functions.catch_input(1, int)
                self.assertEqual(output, 1)
                # 3 "invalid" messages as 3 attempts to input invalid value
                self.assertEqual(mock_out.getvalue(), 
                                 "Invalid input.\nInvalid input.\nInvalid" + 
                                 " input.\nDefault value used.\n")
            
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
        
class TestGetPubFrontDoor(unittest.TestCase):
    def test_outside_buildings(self):
        """
        Test that the returned co-ordinate is not in a building.
        """
        building_coords = drunk_functions.get_building_coords(
                        drunk_functions.import_town("drunk.plan")
                        )
        all_coords = [coord for building_list in \
                      building_coords.values() for coord in building_list]
        output = drunk_functions.get_pub_front_door(building_coords)
        
        self.assertNotIn(output, all_coords)
    
    def test_near_pub(self):
        """
        Test that x and y of the door are within 1 space of the pub.
        """
        building_coords = drunk_functions.get_building_coords(
                        drunk_functions.import_town("drunk.plan")
                        )
        pub_coords = building_coords["pub"]
        output = drunk_functions.get_pub_front_door(building_coords)
        self.assertTrue(any([c[0] - output[0] <= 1 for c in pub_coords]))
        self.assertTrue(any([c[1] - output[1] <= 1 for c in pub_coords]))
        
class TestGetPubBackDoor(unittest.TestCase):
    def test_outside_buildings(self):
        """
        Test that the returned co-ordinate is not in a building.
        """
        building_coords = drunk_functions.get_building_coords(
                        drunk_functions.import_town("drunk.plan")
                        )
        all_coords = [coord for building_list in \
                      building_coords.values() for coord in building_list]
        output = drunk_functions.get_pub_back_door(building_coords)
        
        self.assertNotIn(output, all_coords)
    
    def test_near_pub(self):
        """
        Test that x and y of the door are within 1 space of the pub.
        """
        building_coords = drunk_functions.get_building_coords(
                        drunk_functions.import_town("drunk.plan")
                        )
        pub_coords = building_coords["pub"]
        output = drunk_functions.get_pub_back_door(building_coords)
        self.assertTrue(any([c[0] - output[0] <= 1 for c in pub_coords]))
        self.assertTrue(any([c[1] - output[1] <= 1 for c in pub_coords]))


class TestCreateDrunks(unittest.TestCase):
    def test_length(self):
        """
        Test that the returned list is the correct length.
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        front_door = drunk_functions.get_pub_front_door(building_coords)
        back_door = drunk_functions.get_pub_back_door(building_coords)
        
        output = drunk_functions.create_drunks(town, building_coords,
                                               front_door, back_door,
                                               10, 100)
        self.assertEqual(len(output), 25)
        
    def test_class(self):
        """
        Test that returned list is a list of instances of the drunk class.
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        front_door = drunk_functions.get_pub_front_door(building_coords)
        back_door = drunk_functions.get_pub_back_door(building_coords)
        
        output = drunk_functions.create_drunks(town, building_coords,
                                               front_door, back_door,
                                               10, 100)
        self.assertTrue(all([isinstance(d, drunksframework.Drunk) \
                             for d in output]))
    
class TestGenFunction(unittest.TestCase):    
    def test_past_iterations(self):
        """
        Test that function stops yielding after max number of moves and that
        expected message is printed at this point.
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        front_door = drunk_functions.get_pub_front_door(building_coords)
        back_door = drunk_functions.get_pub_back_door(building_coords)
        drunks = drunk_functions.create_drunks(town, building_coords,
                                               front_door, back_door,
                                               10, 100)
        
        with unittest.mock.patch('sys.stdout', new = StringIO()) as mock_out:
            output = list(drunk_functions.gen_function(2, drunks, town))
            self.assertEqual(mock_out.getvalue(), "0 drunks home in 2 moves.\n")
            self.assertEqual(output, [0, 1])
        
    def test_drunks_home(self):
        """
        Test that function stops yielding after all drunks are home and that
        expected message is printed at this point.
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        front_door = drunk_functions.get_pub_front_door(building_coords)
        back_door = drunk_functions.get_pub_back_door(building_coords)
        drunks = drunk_functions.create_drunks(town, building_coords,
                                               front_door, back_door,
                                               10, 100)
        for drunk in drunks: drunk.is_home = True
        
        with unittest.mock.patch('sys.stdout', new = StringIO()) as mock_out:
            output = list(drunk_functions.gen_function(300, drunks, town))
            self.assertEqual(mock_out.getvalue(), "All drunks home in 0 moves.\n")
            self.assertEqual(output, [])

class TestDrunkMove(unittest.TestCase):
    def test_coord_change(self):
        """
        Test that drunk's coordinates do change as expected.
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        drunk = drunksframework.Drunk(10, 50, 50, town, building_coords, 50)
        drunk.speed = 1
        drunk.move()
        self.assertIn((drunk.x,drunk.y), [(50, 51), (51,50), (49,50), (50,49)])
        
    def test_town_change(self):
        """
        Test that town raster data updates as expected.
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        drunk = drunksframework.Drunk(10, 50, 50, town, building_coords, 50)
        
        # Town at drunk's old position increased by 1
        a = town[50][50]
        drunk.move()
        b = town[50][50]
        self.assertEqual(a, b-1)
        
    def test_town_unchanged(self):
        """
        Test that town is currently unchanged in drunk's new posiiton (old
        position should be only change to town).
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        drunk = drunksframework.Drunk(10, 50, 50, town, building_coords, 50)
        drunk.move()
        self.assertEqual(town[drunk.y][drunk.x], 0)
        
class TestDrunkSoberUp(unittest.TestCase):
    def test_drunk_level(self):
        """
        Test that a drunk's drunk_level decreases by 1.
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        drunk = drunksframework.Drunk(10, 50, 50, town, building_coords, 50)
        # Add current coord to history so drunk will sober up
        drunk.history.append((50,50))
        drunk.sober_up()
        self.assertEqual(drunk.drunk_level, 49)
    
    def test_speed_change(self):
        """
        Test that drunk will change speed as it sobers up.
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        drunk = drunksframework.Drunk(10, 50, 50, town, building_coords, 50)
        
        drunk.drunk_level = 25
        drunk.sober_up()
        self.assertEqual(drunk.speed, 3)
        
        drunk.drunk_level = 10
        drunk.sober_up()
        self.assertEqual(drunk.speed, 5)
    
    def test_history(self):
        """
        Test that drunk's position is added to history.
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        drunk = drunksframework.Drunk(10, 50, 50, town, building_coords, 50)
        
        drunk.sober_up()
        self.assertIn((50,50), drunk.history)
    
    def test_sober_drunk(self):
        """
        Test that a drunk with drunk_level of 0 is handled as expected.
        """
        town = drunk_functions.import_town("drunk.plan")
        building_coords = drunk_functions.get_building_coords(town)
        drunk = drunksframework.Drunk(10, 50, 50, town, building_coords, 0)
        
        drunk.sober_up()
        self.assertEqual(drunk.speed, 5)
        self.assertEqual(drunk.drunk_level, 0)
        self.assertIn((50,50), drunk.history)
        