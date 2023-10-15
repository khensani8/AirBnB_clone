#!/usr/bin/python3
"""Unittest for the BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_base_model_id_generation(self):
        # Create two instances and ensure their IDs are unique
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_to_dict_method(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertTrue('id' in base_model_dict)
        self.assertTrue('created_at' in base_model_dict)
        self.assertTrue('updated_at' in base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

    def test_update_attributes(self):
        base_model = BaseModel()
        base_model.name = "Test Model"
        self.assertEqual(base_model.name, "Test Model")


if __name__ == '__main__':
    unittest.main()
