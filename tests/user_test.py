import json
from unittest import TestCase
from user import User



class TestUser(TestCase):
    path_to_test_json_file = 'users_data_test.json'
    def test_creating_user(self):
        self.assertEqual(User('vasya', True, 50).__dict__,
                         {'balance': 50, 'is_new_person': True, 'user_name': 'vasya'})

    def test_get_balance_if_user_is_new(self):
        self.assertEqual(User.get_balance('unknown',True),100)
    def test_get_balance_if_user_is_not_new(self):
        self.assertEqual(User.get_balance('vasya',False,self.path_to_test_json_file),89)
    def test_checking_is_new_person(self):
        self.assertEqual(User.checking_is_new_person('vasya',self.path_to_test_json_file),True)
        self.assertEqual(User.checking_is_new_person('emildavletov10a', self.path_to_test_json_file), False)





