# tests/test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel
from models.base_model import BaseModel
import json
import unittest
from datetime import datetime
# Test instance creation
my_model = BaseModel()
print(my_model)

# Test id type
print(f"id type: {type(my_model.id)}")

# Test created_at type
print(f"created_at type: {type(my_model.created_at)}")

# Test 2 instances creation with different ids
another_model = BaseModel()
print(f"Another model id: {another_model.id}")

# Test __str__ implementation
print(my_model.__str__())

# Test to_dict()
my_model_dict = my_model.to_dict()
print(my_model_dict)

# Test save() and updated_at type
my_model.save()
print(f"updated_at type: {type(my_model.updated_at)}")
class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_method(self):
        my_model = BaseModel()
        str_representation = str(my_model)
        self.assertIn("[BaseModel]", str_representation)
        self.assertIn(str(my_model.id), str_representation)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        self.assertIsInstance(my_model_json, dict)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)

    def test_save_method(self):
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_from_dict_creation(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.name, new_model.name)
        self.assertEqual(my_model.my_number, new_model.my_number)
        self.assertEqual(my_model.created_at, new_model.created_at)
        self.assertEqual(my_model.updated_at, new_model.updated_at)

if __name__ == '__main__':
    unittest.main()
