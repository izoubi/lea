__author__ = 'Ismail'

'''
Intent
this file is a class that its instance has two attributes; a math problem type e.x Quadratic Equations,
and a math problem e.x 2y^2 + 4 = 9y.
it has one method which is to open a directory of a math problem file and return its content (answer)
'''


class OpenMathProblem:
    def __init__(self,a_math_problem_type,a_math_problem):  # an instance of the class is created.
        self.math_problem_type = a_math_problem_type
        self.math_problem = a_math_problem

    def open_problem(self):

        # precondition : when this function is called, the class instance should be assigned already a math problem type
                        # and math problem
        # postcondition : content of a math problem file is returned
        # objective 1 : open the file
        # objective 2 : split its content based on \n

        file=open('{}/{}.txt'.format(self.math_problem_type,self.math_problem),'r')  # open the file
        answer_from_file = file.read()  # read the  file (the steps of the solution). objective 1 is carried out
        file.close()  # close the file

        split_answer = answer_from_file.split('\n')  # split the file content. objective 2 is carried out
        return split_answer
