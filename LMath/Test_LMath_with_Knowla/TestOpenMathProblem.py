from LMath_with_Knowla.OpenMathProblem import *
import unittest


class TestOpenMathProblemClass(unittest.TestCase):
    def setUp(self):

        self.math_problem_type = 'Quadratic Equations'
        self.math_problem = '2y^2 + 4 = 9y'
        self.a = OpenMathProblem(self.math_problem_type,self.math_problem)

    def test_open_problem(self):
        self.assertEqual(['2y^2 - 9y + 4 = 0', '(2y-1)(y-4) = 0', '2y - 1 = 0; y-4 = 0', '2y = 1; y = 4',
                         'y = 1/2;y = 4', 'y = {1/2,4}'],self.a.open_problem())


