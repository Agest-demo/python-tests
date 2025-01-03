import unittest
import os

class TestAddition(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
        print(os.getenv('MY_PARAM'))

if __name__ == "__main__":
    unittest.main()