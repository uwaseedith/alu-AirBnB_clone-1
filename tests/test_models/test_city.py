#!/usr/bin/python3
"""
Unittests for city
"""

import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """ Tests the City Class """

    def test_instance(self):
        """ Tests instance """
        obj = City()
        self.assertIsInstance(obj, City)

    def test_is_subclass(self):
        """tests the instance of sub classes"""
        city = City()
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_name(self):
        """tests name"""
        city = City()
        self.assertEqual(city.name, "")
        city.name = "Kigali"
        self.assertEqual(city.name, "Kigali")

    def test_city_id(self):
        """tests city id"""
        city = City()
        self.assertEqual(city.state_id, "")


if __name__ == "__main__":
    unittest.main()