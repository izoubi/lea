import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from LMath_with_Knowla.OpenMathProblem import *
from LMath_with_Knowla.findout_user_inputs import *
from LMath_with_Knowla.OpenMathProblemFolder import *
import tkinter.messagebox
from LMath_with_Knowla.Calculate import *
import random

__author__ = 'Ismail'

'''
INTENT : this class's instance has an attribute (master), it's the root of the main window.
it has a method to create widgets and place them in the main window
the widgets in the form in this class are the ones that the user will select math problems and answer them
'''
user_grade_second_option = 0
# this variable will be used to save the user's grade if the second way of using the program is selected.


class InteractionInterface(Frame):
    def __init__(self,master,char_representing_selected_way):
        Frame.__init__(self,master)
        self.way_using_program = char_representing_selected_way
        self.split_answer_for_problem = []
        #  this list will be assigned the correct answer of the selected math problem.
        self.create_widgets()

    def create_widgets(self):
        self.interaction_frame = ttk.Frame(self.master, width=600, height=400)  # create a frame inside the master
        self.interaction_frame['relief'] = 'sunken'
        self.interaction_frame['borderwidth'] = 2
        self.interaction_frame.place(x=700/2-600/2, y=500/2-400/2)

        # from this point, all the widgets are created inside the frame not the master.
        self.chooseCategoryLabel = ttk.Label(self.interaction_frame,wraplength=200,
                                             text="Choose the type of problem you want to work on")
        self.chooseCategoryLabel.place(x=0,y=0)

        self.options = ['Linear Equations', 'Quadratic Equations', 'Rational Polynomial Equations']
        # the types of math problems
        self.options.insert(0, "Choose a category")
        self.selected_math_problem_type = tk.StringVar()  # assigned the selected math problem type
        self.selected_math_problem_type.set(self.options[0])  # default value
        self.problem_type = tk.OptionMenu(self.interaction_frame, self.selected_math_problem_type, *self.options,
                                          command=self.show_math_problems)  # option menu for the math problem types.
        # its command is to show problems related to the selected math problem type
        self.problem_type.focus_set()
        self.problem_type.place(x=0,y=40)
        self.problem_type.bind("<Return>", lambda x: self.show_math_problems())

        self.problems = Listbox(self.interaction_frame, selectmode=SINGLE)  # create a list box shows math problems
        self.problems.focus_set()
        self.problems.place(x=10,y=70)
        self.problems.bind('<<ListboxSelect>>', lambda x: self.open_math_problem(bind_type=1))  # open math problem.
        self.problems.bind("<Return>", lambda x: self.open_math_problem(bind_type=2))

        self.shuffled_answer_lbl = ttk.Label(self.interaction_frame, wraplength=162,
                                             text="the answer sorted incorrectly:")
        self.shuffled_answer_lbl.place(x=219,y=35)

        self.shuffled_answer = tk.Listbox(self.interaction_frame, selectmode=SINGLE)  # the answer is displayed here
        self.shuffled_answer.place(x=219,y=70)

        self.user_answer_lbl = ttk.Label(self.interaction_frame, text="your answer ")  # label to user's answer
        self.user_answer_lbl.place(x=428,y=35)

        self.user_answer = tk.Listbox(self.interaction_frame, selectmode=SINGLE)  # user's answer listbox
        # call this function if the item in user answer list box is clicked by the left mouse button
        self.user_answer.bind('<Button-1>', self.set_current)
        # call this function if the item in user answer list box is clicked by the left mouse button and moved
        # while clicking
        self.user_answer.bind('<B1-Motion>', self.shift_selection)

        self.user_answer.curIndex = None
        self.user_answer.place(x=428,y=70)

        self.submit_btn = ttk.Button (self.interaction_frame, text ="submit", command=self.calc_grade_first_option)
        # submit button to calculate user's grade.
        self.submit_btn.bind("<Return>", lambda x: self.calc_grade_first_option())

        self.submit_btn.place(x=428,y=250)

        self.grade_Label = ttk.Label(self.interaction_frame, wraplength=162,
                                     text="your grade")  # label to show user's grade
        self.grade_Label.place(x=428,y=290)

        self.percentage_Label = ttk.Label(self.interaction_frame,wraplength=162,text="your grade percentage ")
        # label to show user's grade percentage
        self.percentage_Label.place(x=428,y=340)

        if self.way_using_program == 'a':
            # check how the user selected the way of using the program
            self.master.title("LMAth with Knowla\Get a grade at the end")  # change main menu title

            # call the function that moves the answer steps to user's answer listbox
            # based on choice a of using the program
            self.shuffled_answer.bind('<<ListboxSelect>>', lambda x: self.move_to_user_answer_choice_a(bind_type=1))
            self.shuffled_answer.bind("<Return>",lambda x: self.move_to_user_answer_choice_a(bind_type=2))

        elif self.way_using_program == 'b':
            self.submit_btn.place_forget()  # remove submit button
            self.master.title("LMAth with Knowla\grade while you answer plus feedback")  # change main menu title

            # call the function that moves the answer steps to user's answer listbox
            # based on choice b of using the program
            self.shuffled_answer.bind('<<ListboxSelect>>',lambda x: self.move_to_user_answer_choice_b_c(bind_type=1))
            self.shuffled_answer.bind("<Return>", lambda x: self.move_to_user_answer_choice_b_c(bind_type=2))

        elif self.way_using_program == 'c':
            for widget in [self.submit_btn, self.grade_Label, self.percentage_Label]:
                widget.place_forget()  # remove the widgets in the loop from the frame

            self.master.title("LMAth with Knowla\plus feedback")  # change main menu title

            #  call the function to move the answers.
            self.shuffled_answer.bind('<<ListboxSelect>>',lambda x: self.move_to_user_answer_choice_b_c(bind_type=1))
            self.shuffled_answer.bind("<Return>", lambda x: self.move_to_user_answer_choice_b_c(bind_type=2))

        for widget in [self.problems, self.shuffled_answer, self.user_answer]:  # loop through all the list boxes
            widget.bind_all("<Key>", self.on_up_down_key_problems_listbox)  # bind if there is a keyboard key clicked



    def show_math_problems(self, *args):
        # precondition : a math problem type is selected.
        # postcondition : math problems are displayed in a list box
        global user_grade_second_option
        user_grade_second_option = 0  # set user's grade to 0.
        self.grade_Label.config(text= 'your grade ')
        self.percentage_Label.config(text='your grade percentage ')
        self.submit_btn.config(state='normal')  # active submit_answer button
        for widget in [self.problems, self.shuffled_answer, self.user_answer]:
            widget.delete(0, END)  # delete all the items in the list boxes in the loop

        the_selected_problem_type = self.selected_math_problem_type.get()  # get what problem type the user selected.

        # create an instance of OpenMathProblemFolder class
        self.problem_type_user_choice = OpenMathProblemFolder(the_selected_problem_type)

        # invoke the class function that returns the math problems
        math_problem_for_selected_type = self.problem_type_user_choice.show_problems()

        for index in range(len(math_problem_for_selected_type)):
            self.problems.insert(END, math_problem_for_selected_type[index])
            # insert the math problems in their listbox

    def open_math_problem(self, *args, bind_type):
        # preconditions : the math problem type and the problem are selected
        # postcondition : displayed solution.
        global user_grade_second_option
        key = int(bind_type)  # used to know if the user uses the mouse or the keyboard.
        if tk.messagebox.askyesno("Note", "Are you sure?") == FALSE:
            pass
        elif self.problems.curselection() or self.problems.get(ACTIVE):
            user_grade_second_option = 0  # set user's grade to 0
            self.grade_Label.config(text='your grade ')
            self.percentage_Label.config(text='your grade percentage ')
            self.submit_btn.config(state='normal')  # active submit_answer button
            self.shuffled_answer.delete(0,END)  # delete all the items in the answer list box
            self.user_answer.delete(0,END)  # delete all the items in the user answer list box
            if key == 1:
                # find out the index of the selected problem in the listbox
                selected_problem_index = int(self.problems.curselection()[0])
                # get the value of the selected problem
                self.selected_problem = self.problems.get(selected_problem_index)

            elif key == 2 and self.problems.get(ACTIVE):
                self.selected_problem = self.problems.get(ACTIVE)  # get the active item in the case of using return key

            self.the_selected_math_problem_type = self.selected_math_problem_type.get()  # selected problem type.

            # create an instance of OpenMathProblem class with attributes of the selected math problem type
            # and the selected math problem
            a_math_problem = OpenMathProblem(str(self.the_selected_math_problem_type), str(self.selected_problem))

            split_answer = a_math_problem.open_problem()  # invoke open problem function to return the solution

            self.showed_answer = split_answer
            self.split_answer_for_problem = split_answer.copy()  # copy the solution to this class attribute
            random.shuffle(self.showed_answer)

            for index in range(len(split_answer)):
                # insert the steps of the solution in shuffled answer list box
                self.shuffled_answer.insert(END, split_answer[index])
        else:
            # if the list box has no items, a warning pop up message is showed
            tk.messagebox.showwarning("WARNING","no problems to select, please select problem type first")

    def move_to_user_answer_choice_a(self, *args, bind_type ):
        # precondition : a solution of the selected problem is displayed in the shuffled answer listbox
        # postcondition : the steps of solution are in user's answer listbox
        key = int(bind_type)
        if tk.messagebox.askyesno("Note", "Are you sure?") == FALSE:
            pass
        elif self.shuffled_answer.curselection() or self.shuffled_answer.get(ACTIVE):
            if key == 1:
                selected_answer_step_index = int(self.shuffled_answer.curselection()[0])
                selected_answer_step_value = self.shuffled_answer.get(selected_answer_step_index)
            elif key == 2:
                selected_answer_step_value = self.shuffled_answer.get(ACTIVE)

            # insert the selected solution step to user's answer listbox
            self.user_answer.insert(END, selected_answer_step_value)

            # to delete the step from the shuffled steps list box
            if key == 2:
                self.shuffled_answer.delete(ACTIVE)
            elif key ==1:
                self.shuffled_answer.delete(selected_answer_step_index)

        else:
            tk.messagebox.showwarning("WARNING","there are no answer steps to select")

    def calc_grade_first_option(self):
        try:
            user_answer_list = []
            for i, listbox_entry in enumerate(self.user_answer.get(0, END)):
                # append all the items in user's answer list box in his answer list
                user_answer_list.append(self.user_answer.get(i))

            # call this function to find out the user's input against the correct answer
            user_accurate_input = get_user_solution_input(self.split_answer_for_problem, user_answer_list)

            # create an instance of Calculate class
            problem_grading = Calculate(user_accurate_input, len(self.split_answer_for_problem))
            user_grade_first_option = problem_grading.get_user_grade()
            total_grade_first_option = problem_grading.get_total_grade()
            user_grade_percentage = problem_grading.get_user_grade_percentage()

            # display the grade and its percentage in their labels
            self.grade_Label.config(text= 'your grade is '+ str(user_grade_first_option) + ' out of ' +
                                          str(total_grade_first_option))
            self.percentage_Label.config(text='your grade percentage is '+str(user_grade_percentage)+"%")

            self.submit_btn.config(state='disabled')  # disable the submit button after it's been clicked

        except ZeroDivisionError:
            tk.messagebox.showwarning("Error", "There are no selected steps"+"\n"+"No grade could be calculated")

    def move_to_user_answer_choice_b_c(self, *args, bind_type):
        key = int(bind_type)
        if tk.messagebox.askyesno("Note","Are you sure?") == FALSE:
            pass
        elif self.shuffled_answer.curselection() or self.shuffled_answer.get(ACTIVE):
            if key == 1:
                selected_answer_step_index = int(self.shuffled_answer.curselection()[0])
                selected_answer_step_value = self.shuffled_answer.get(selected_answer_step_index)
            elif key == 2:
                selected_answer_step_value = self.shuffled_answer.get(ACTIVE)

            # insert the selected answer step to user's answer listbox
            self.user_answer.insert(END, selected_answer_step_value)

            if key == 2:
                self.shuffled_answer.delete(ACTIVE)
            elif key ==1:
                self.shuffled_answer.delete(selected_answer_step_index)

            size_user_answer = self.user_answer.size()  # get the size of the user's answer listbox
            user_answer_last_item_index = int(size_user_answer-1)

            # add _note for the problem name to open the file that contains comments for the selected problem
            self.name_file_note = self.selected_problem+"_note"

            # create an instance of openmath problem class to open the notes file.
            a_math_problem_note = OpenMathProblem(str(self.the_selected_math_problem_type), str(self.name_file_note))

            # invoke open math problem to return the file that contains the comments for the selected problem
            self.split_answer_note = a_math_problem_note.open_problem()

            # checking if the selected answer is correct or wrong
            self.condition = self.user_answer.get(int(user_answer_last_item_index)) != \
                                 self.split_answer_for_problem[user_answer_last_item_index]

            if self.condition == TRUE:
                # a feedback is showed if the answer is wrong
                tk.messagebox.showerror("Error", "this choice is wrong! \n" +
                                            self.split_answer_note[user_answer_last_item_index])

                # delete the selected answer from user's answer listbox
                self.user_answer.delete(user_answer_last_item_index, user_answer_last_item_index)

                # insert the answer back to the shuffled answer listbox
                self.shuffled_answer.insert(END,selected_answer_step_value)
            else:
                pass

            if self.way_using_program == 'b':
                self.calc_second_option()  # call the function that calculates the user's grade after each step.
            else:  # if the way of using the program is 'c', then no grade is calculated
                pass
        else:
            tk.messagebox.showwarning("Error","there are no answer steps to select")

    def calc_second_option(self):
        # precondition : there are an answer steps has been selected.
        # postcondition : every step's grade is calculated, & grade's percentage is calculated at the end
        global user_grade_second_option  # use the global variable.
        number_steps = len(self.split_answer_for_problem)
        total_grade = int(number_steps)
        correct_step_grade = float(total_grade/total_grade)  # the correct answer grade's fragment
        wrong_step_answer = float(total_grade/total_grade/2)  # the wrong answer grade's fragment

        if self.condition == TRUE:
            user_grade_second_option -= wrong_step_answer
        else:
            user_grade_second_option += correct_step_grade

        # update the grade label
        self.grade_Label.config(text= 'your grade is ' + str(user_grade_second_option) + ' out of ' + str(total_grade))

        size_user_answer = int(self.user_answer.size())
        if size_user_answer == total_grade:  # if the user selects all the answer steps, the percentage is calculated
            grade_percentage = user_grade_second_option/total_grade*100
            grade_percentage = round(grade_percentage, 2)
            self.percentage_Label.config(text='your grade percentage is  ' +
                                              str(grade_percentage) + "%")

            # after displaying the grade and the percentage, set it to 0 to be used again because it's a global variable
            user_grade_second_option = 0
    '''
    if the way of using the program is 'a', then the next two functions are used to drag and drop the items in
    the answer list box in order to sort them before the user submits his/her answer.
    '''
    def set_current(self, event):
        # check how the user selected the way of using the program
        if self.way_using_program != 'a':
            pass
        else:
            # place the item of the user's answer list box after being moved.
            self.user_answer.curIndex = self.user_answer.nearest(event.y)

    def shift_selection(self, event):
        if self.way_using_program != 'a':  # check how the user selected the way of using the program
            pass
        else:
            # move the item in user's list box in different order within the same listbox
            i = self.user_answer.nearest(event.y)
            if i < self.user_answer.curIndex:
                x = self.user_answer.get(i)
                self.user_answer.delete(i)
                self.user_answer.insert(i+1, x)
                self.user_answer.curIndex = i
            elif i > self.user_answer.curIndex:
                x = self.user_answer.get(i)
                self.user_answer.delete(i)
                self.user_answer.insert(i-1, x)
                self.user_answer.curIndex = i

    @staticmethod
    def on_up_down_key_problems_listbox(event):  # make the active key highlighted in blue.
        try:
            if event.keysym == 'Up':  # if the 'up' key is clicked.
                event.widget.select_clear(0, END)
                event.widget.select_clear(0, END)
                event.widget.select_set(ACTIVE)
                event.widget.activate(ACTIVE)
            if event.keysym == 'Down':  # if the 'down' key is clicked.
                event.widget.select_clear(0, END)
                event.widget.select_set(ACTIVE)
                event.widget.activate(ACTIVE)
        except:
            pass