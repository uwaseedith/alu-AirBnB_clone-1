#!/usr/bin/python3
"""
Unittest for amenity
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """ Tests the Amenity class """

    def test_instance(self):
        """ Tests instance """
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_is_subclass(self):
        """tests the instance of sub classes"""
        amenity = Amenity()
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_name(self):
        """tests name"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")
        self.assertIsNotNone(amenity.id)


if __name__ == "__main__":
    unittest.main()