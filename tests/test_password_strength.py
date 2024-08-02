import unittest
from password_generator import password_generator

class TestPasswordGenerator(unittest.TestCase):

    def test_empty_password(self):
        self.assertEqual(password_generator(0), '')

    def test_default_includes(self):
        password = password_generator(10)
        self.assertEqual(len(password), 10)
        # Check if the password contains only allowed characters
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@%!#$^&*")
        self.assertTrue(all(char in allowed_chars for char in password))
    
    def test_custom_includes(self):
        password = password_generator(10, includes=[1, 3])
        self.assertEqual(len(password), 10)
        # Check if the password contains only lowercase letters and digits
        allowed_chars = set("abcdefghijklmnopqrstuvwxyz0123456789")
        self.assertTrue(all(char in allowed_chars for char in password))

    def test_check_strength(self):
        password, strength = password_generator(10, check_strength=True)
        self.assertEqual(len(password), 10)
        self.assertIsInstance(strength, str)
    
    def test_invalid_includes(self):
        password = password_generator(10, includes="invalid")
        self.assertEqual(len(password), 10)
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@%!#$^&*")
        self.assertTrue(all(char in allowed_chars for char in password))

if __name__ == '__main__':
    unittest.main()
