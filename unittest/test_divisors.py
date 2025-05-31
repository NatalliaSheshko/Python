import unittest
from divisors import *

class TestFindDivisors(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(find_divisors(10), [1, 2, 5, 10])

    def test_positive_number_2(self):
        self.assertCountEqual(find_divisors(10), [2, 1, 5, 10])

    def test_prime_number(self):
        self.assertEqual(find_divisors(13), [1, 13])

    def test_zero_number(self):
        self.assertEqual(find_divisors(0), [])

    def test_one_number(self):
        self.assertEqual(find_divisors(1), [1])

    def test_negative_number(self):
        self.assertEqual(find_divisors(-10), [1, 2, 5, 10])

if __name__ == '__main__':
    unittest.main()
