import unittest
from dog import *

class TestDogToHumanAge(unittest.TestCase):
    def test_dog_age_1(self):
        self.assertEqual(dog_to_human_age(1), 14)

    def test_dog_age_2(self):
        self.assertEqual(dog_to_human_age(2), 22)

    def test_dog_age_3(self):
        self.assertEqual(dog_to_human_age(3), 27)

if __name__ == '__main__':
    unittest.main()
