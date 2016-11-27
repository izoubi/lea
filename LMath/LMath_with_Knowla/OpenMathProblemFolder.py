import os

__author__ = 'ismail'

'''
Intent
this file is a class that its instance has one attribute; a math problem type e.x Quadratic Equations,
it has one method which is to open a directory, find the folder of math problem type and retrieve its content (files).
the files are two types, one type contains steps to solve such a problem and one the second types contains comments.
this method will return only the ones that contain solution steps.
'''


class OpenMathProblemFolder:
    def __init__(self, a_problem_type):   # an instance of the class is created.
        self.problem_type = a_problem_type

    def show_problems(self):
        # precondition : when this function is called, the class instance should be assigned already a math problem type
        # postcondition : all the files' names in the folder of math problem type are found out

        root_dir = self.problem_type  # identify the folder (problem type folder)that was selected by the user.

        full_directory =[]
        for subdir, dirs, files in os.walk(root_dir):  # go through all the files and save each one's name in a list
            for file in files:
                full_directory.append(os.path.join(subdir, file))  # the list have items of folder name/filename.txt
                # e.g one element will be Quadratic Equations/2y^2 + 4 = 9y.txt

        full_directory_separated_by_backslash = []  # e.g ['Quadratic Equations', '2y^2 + 4 = 9y.txt']
        full_problem_name_with_extension = []  # e.g ['2y^2 + 4 = 9y.txt']
        full_problem_name_with_extension_separated_from_dot = []  # e.g ['2y^2 + 4 = 9y', 'txt']
        problem_name_without_extension = []  # e.g ['2y^2 + 4 = 9y']

        for first_index in range (0,len(full_directory)):  # the loop go through all the items in list of full directory
            temp = full_directory[first_index]
            full_directory_separated_by_backslash = temp.split('\\')  # split the element by \\
            full_problem_name_with_extension.append(full_directory_separated_by_backslash[1])
            # append to the list  only the second part of full directory which  is 2y^2 + 4 = 9y.txt

        for second_index in range(len(full_problem_name_with_extension)):
            # go through all items in the list that its items are problem.txt
            second_temp = full_problem_name_with_extension[second_index]
            full_problem_name_with_extension_separated_from_dot=second_temp.split('.')  # split each element by .
            if "_note" not in full_problem_name_with_extension_separated_from_dot[0]:
                # if the problem name doesn't contain "_note" in it, then it's appended
                problem_name_without_extension.append(full_problem_name_with_extension_separated_from_dot[0])
                # append d array only the name of the problem and discard .txt . e.g d array has only 2y^2 + 4 = 9y

        return problem_name_without_extension



