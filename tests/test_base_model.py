import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_base_model_attributes(self):
        # Create an instance of the BaseModel class
        base_model = BaseModel()

        # Check if the attributes are set correctly
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_base_model_save(self):
        # Create an instance of the BaseModel class
        base_model = BaseModel()

        # Save the BaseModel instance
        base_model.save()

        # Check if the updated_at attribute is updated
        self.assertNotEqual(base_model.created_at, base_model.updated_at)

    def test_base_model_to_dict(self):
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


if __name__ == '__main__':
    unittest.main()
