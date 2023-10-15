#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser(unittest.TestCase)
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        # Initialize any necessary setup for the tests
        self.user = User()

    def test_user_attributes(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_id_generation(self):
        # Assuming your BaseModel implementation generates unique IDs
        self.assertIsNotNone(self.user.id)

    def test_to_dict_method(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)


if __name__ == "__main__":
    unittest.main()
