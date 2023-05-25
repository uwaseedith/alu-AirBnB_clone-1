#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import os


class TestBaseModel(unittest.TestCase):

    def test_base_model_attributes(self):
        # Create an instance of the BaseModel class
        base_model = BaseModel()

        # Check if the attributes are set correctly
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(base_model.created_at, base_model.updated_at)
    
    def test_instantiation_with_kwargs(self):
        # 1. We create a new instance of the BaseModel class.
        # 2. We set the id attribute to “345”.
        # 3. We set the created_at attribute to the current time.
        # 4. We set the updated_at attribute to the current time.
        # 5. We check that the id attribute is set to “007”.
        # 6. We check that the created_at attribute is set to the current time.
        # 7. We check that the updated_at attribute is set to the current time.
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="007", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "007")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


    def test_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_to_dict(self):
        # Create an instance of the BaseModel class
        base_model = BaseModel()

        # Convert the BaseModel instance to a dictionary
        base_model_dict = base_model.to_dict()

        # Check if the dictionary contains the required keys
        self.assertIn('__class__', base_model_dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

        # Check if the class name is correct
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

        # Check if the datetime attributes are in ISO format
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)

    def test_base_model_str(self):
        # Create an instance of the BaseModel class
        base_model = BaseModel()

        # Check if the string representation is correct
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

class TestBaseModel_save(unittest.TestCase):
    """
        Unittests to test save method of the 'BaseModel' class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())
if __name__ == '__main__':
    unittest.main()
