#!/usr/bin/python3
"""
Unittests for state class
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test the State class"""

    def test_instance(self):
        """Tests instance"""
        obj = State()
        self.assertIsInstance(obj, State)

    def test_is_subclass(self):
        """Tests subclass"""
        obj = State()
        self.assertTrue(issubclass(type(obj), BaseModel))

    def test_name(self):
        """Tests name"""
        obj = State()
        self.assertEqual(obj.name, "")
        obj.name = "Betty"
        self.assertEqual(obj.name, "Betty")

    def test_str(self):
        """Test str"""
        obj = State()
        string = "[State] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), string)


if __name__ == "__main__":
    unittest.main()