from LMath_with_Knowla.Calculate import *
import unittest


class TestCalculate(unittest.TestCase):
    def setUp(self):

        self.user_response = [1, 2, 3, 4]
        self.problem_grading = Calculate(self.user_response,4)

    def test_get_user_grade(self):
        self.assertEqual(6,self.problem_grading.get_user_grade())

    def test_get_total_grade(self):
        self.assertEqual(6,self.problem_grading.get_total_grade())

    def test_get_user_grade_percentage(self):
        self.assertEqual(100, self.problem_grading.get_user_grade_percentage())