from LMath_with_Knowla.OpenMathProblemFolder import *
import unittest


class TestUserChoiceClass(unittest.TestCase):
    def setUp(self):

        self.math_problem_type = 'Quadratic Equations'
        self.a = OpenMathProblemFolder(self.math_problem_type)

    def test_show_problems(self):
        self.assertEqual(['2y^2 + 4 = 9y', 'problem02', 'problem03'],self.a.show_problems())


