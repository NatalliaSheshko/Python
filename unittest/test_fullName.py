import unittest
import fullName


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(
            fullName.fullName('Шешко', 'Наталья', 'Анатольевна'),
            'Шешко Наталья Анатольевна')

    def test_big(self):
        self.assertEqual(
            fullName.fullName('ШЕШКО','НАТАЛЬЯ','АНАТОЛЬЕВНА'), 'Шешко Наталья Анатольевна'
        )

    def test_small(self):
        self.assertEqual(
            fullName.fullName('шешко','натлья','анатольевна'),'Шешко Натлья Анатольевна'
        )


if __name__ == '__main__':
    unittest.main()
