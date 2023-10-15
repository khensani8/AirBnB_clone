#!/usr/bin/python3
"""Module for test Amenity class"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up an Amenity instance for testing.
        """
        self.amenity = Amenity()
        self.amenity.name = "Swimming Pool"

    def tearDown(self):
        """
        Clean up after testing.
        """
        del self.amenity

    def test_instance_attributes(self):
        """
        Test if Amenity instance has the expected attributes.
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'to_dict'))

    def test_instance_attributes_types(self):
        """
        Test the types of attributes in the Amenity instance.
        """
        self.assertEqual(type(self.amenity.name), str)
        self.assertEqual(type(self.amenity.created_at), datetime)
        self.assertEqual(type(self.amenity.updated_at), datetime)
        self.assertEqual(type(self.amenity.id), str)

    def test_save(self):
        """
        Test the save method in Amenity.
        """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method in Amenity.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(type(amenity_dict), dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], 'Swimming Pool')


if __name__ == '__main__':
    unittest.main()
