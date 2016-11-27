__author__ = 'Ismail'


def get_user_solution_input(correct_answer, user_input):
    # precondition : the function receives the correct answer, and the user's answer.
    # postcondition : accurate user input is found out.
    user_solution_input =[]  # this list will contain the accurate user's input comparing with the correct answer.
    for user_input_index in range(0, len(user_input)):
        key = user_input[user_input_index]
        for correct_answer_index in range(0, len(correct_answer)):
            if (correct_answer[correct_answer_index]) == key:  # compare each element in the correct answer against
                                                                #  user's input
                user_solution_input.append(correct_answer_index+1)
                break  # terminate the internal loop if the condition is TRUE
    return user_solution_input  # return the user's input ( accurate )

