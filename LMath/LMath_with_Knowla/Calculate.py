__author__ = 'ismailzoubi'


class Calculate:
    def __init__(self, a_user_response, a_correct_solution_length):
        self.user_response = a_user_response
        self.correct_solution_length = int(a_correct_solution_length)

    def get_user_grade(self):
        # precondition : the function receives a list (answer) in the from of number from one to how many steps
                    #in the answer.
        # postcondition :  a grade is calculated.

        number_answers = len(self.user_response)  # find out the length of the user's response.
        grade = 0
        for index_one in range(0, number_answers - 1):
            for index_two in range(index_one + 1, number_answers):
                if self.user_response[index_one] < self.user_response[index_two]:  # comparing each element with its followings.
                    grade += 1
        return grade  # return the calculated grade.

    def get_total_grade(self):
       # user_response_length = len(self.user_response)
        return self.correct_solution_length * (self.correct_solution_length-1) / 2
    
    def get_user_grade_percentage(self):
        # precondition :  the function receives a grade and a total grade
        # postcondition : the grade percentage is calculated
        user_grade = self.get_user_grade()
        total_grade = self.get_total_grade()
        return round(100 * user_grade/total_grade)  # returning the grade's percentage.

