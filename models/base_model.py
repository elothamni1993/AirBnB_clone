# tests/test_base_model.py

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        """Test instance creation."""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_instance_creation_id_type(self):
        """Test instance creation + id type."""
        instance = BaseModel()
        self.assertTrue(isinstance(instance.id, str))

    def test_instance_creation_created_at_type(self):
        """Test instance creation + created_at type."""
        instance = BaseModel()
        self.assertTrue(isinstance(instance.created_at, datetime))

    def test_instances_creation_different_id(self):
        """Test 2 instances creation + id different."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_instance_creation_str_implementation(self):
        """Test instance creation + __str__ implementation."""
        instance = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(instance.id, str(instance.__dict__))
        self.assertEqual(str(instance), expected_str)

    def test_instance_creation_to_dict(self):
        """Test instance creation + to_dict()."""
        instance = BaseModel()
        expected_dict = {
            'id': instance.id,
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat(),
        }
        self.assertEqual(instance.to_dict(), expected_dict)

    def test_instance_creation_save_updated_at_type(self):
        """Test instance creation + save() + updated_at type."""
        instance = BaseModel()
        instance.save()
        self.assertTrue(isinstance(instance.updated_at, datetime))

    def test_base_model_save(self):
        """Test BaseModel: save()."""
        instance = BaseModel()
        initial_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(initial_updated_at, instance.updated_at)

    def test_base_model_to_dict(self):
        """Test BaseModel: to_dict()."""
        instance = BaseModel()
        expected_dict = {
            'id': instance.id,
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat(),
        }
        self.assertEqual(instance.to_dict(), expected_dict)

    def test_base_model_self_id(self):
        """Test BaseModel: self.id."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, 'id'))

    def test_base_model_self_created_at(self):
        """Test BaseModel: self.created_at."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, 'created_at'))

    def test_base_model_str(self):
        """Test BaseModel: __str__(self)."""
        instance = BaseModel()
        self.assertTrue(str(instance))

