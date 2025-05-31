import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up some stuff for [" + self.shortDescription() + "]")
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after [" + self.shortDescription() + "]")

    def test_store_single_response(self):
        """Проверяет, что один ответ сохранен правильно."""
        question = "Какой язык программирования вам по душе?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Java')
        self.assertIn('Java', my_survey.responses)

    def test_fife_responses(self):
        """Проверяет, что пять ответов были сохранены"""
        question = "Какой язык программирования вам по душе?"
        my_survey = AnonymousSurvey(question)

        responses = ['Java', 'Python', 'C#', 'Go', 'JavaScript']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()

