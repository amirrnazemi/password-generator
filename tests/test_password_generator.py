import unittest
from password_checker import check_password_strength

class TestPasswordGenerator(unittest.TestCase):

    def test_very_weak(self):
        self.assertEqual(check_password_strength("123"), 'very weak')
    
    def test_weak(self):
        self.assertEqual(check_password_strength("12345"), 'weak')

    def test_medium(self):
        self.assertEqual(check_password_strength("12345678912"), 'medium')
    
    def test_strong(self):
        self.assertEqual(check_password_strength("123456789012345"), 'strong')
    
    def test_very_strong(self):
        self.assertEqual(check_password_strength("12345678901234567890"), 'very strong')
    
    def test_tagged_false(self):
        self.assertEqual(check_password_strength("123", tagged=False), 15)
        self.assertEqual(check_password_strength("12345678901234567890", tagged=False), 100)

if __name__ == '__main__':
    unittest.main()
