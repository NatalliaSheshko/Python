import unittest
from even import *

class TestIsEven(unittest.TestCase):

    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_testing(self):
        self.assertEqual(is_even(4), True)

    def test_odd_number(self):
        self.assertFalse(is_even(5))

    def test_zero(self):
        self.assertTrue(is_even(0))

    def test_negative_number(self):
        self.assertTrue(is_even(-2))


if __name__ == '__main__':
    unittest.main()
