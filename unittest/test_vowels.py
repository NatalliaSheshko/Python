import unittest
from vowels import *

class Test_Vowels(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello'), 2)

    def test_count_uppercase(self):
        self.assertEqual(count_vowels('hellO'), 2)

    def test_count_empty(self):
        self.assertEqual(count_vowels(''), 0)

    def test_count_no_vowels(self):
        self.assertEqual(count_vowels('wrtp'), 0)

    def test_count_all_vowels(self):
        self.assertEqual(count_vowels('aeiouAEIOU'), 10)


if __name__ == '__main__':
    unittest.main()
