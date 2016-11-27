
from Interface_LMath_with_Knowla.InteractionInterface import InteractionInterface
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox


__author__ = 'Ismail'

'''
INTENT : this class's instance has an attribute (master), it's the root of the main window.
it has a method to create widgets and place them in the main window
'''

class UseAppInterface(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.create_widgets()

    def create_widgets(self):
        self.frame_use_app = ttk.Frame(self.master, width=400, height=300)  # create a frame in the master
        self.frame_use_app['relief'] = 'sunken'
        self.frame_use_app['borderwidth'] = 2
        self.frame_use_app.place(x=700/2-400/2, y=500/2-300/2)

        # from here and so on, all widgets are created inside the frame not the main window.
        self.select_way_label = ttk.Label (self.frame_use_app, text="Please! choose how you will use the program")
        select_way_label_size = int(self.select_way_label.winfo_reqwidth())
        self.select_way_label.place(x=400/2-select_way_label_size/2,y=20)

        use_program_selection = [
            ('Grading at the End', 'a'),
            ('Grading While You Answer with Feedback', 'b'),
            ('Feedback Only with no Grading', 'c')]  # the options of using the program

        self.char_representing_selected_way = StringVar()
        self.char_representing_selected_way.set('a')  # default selected way is Grading at the End

        increment = 30
        placing_in_y_axis = 70  # used in placing the radio buttons in the vertical axis

        for text, mode in use_program_selection:
            self.way_use_app = ttk.Radiobutton(self.frame_use_app, text=text,
                                               variable=self.char_representing_selected_way, value=mode)
                                               # radiobutton to show ways of using the program
            self.way_use_app.place(x=90, y=int(placing_in_y_axis))  # to place the radio buttons in the frame
            placing_in_y_axis += increment  # increase the y axis so the radio buttons don't overlap

        self.open_interaction_frame_btn = ttk.Button(self.frame_use_app, text="Enter",
                                                     command=self.open_interaction_frame)
                                                    #  a button to move to the next frame

        open_interaction_frame_btn_size = int(self.open_interaction_frame_btn.winfo_reqwidth())
        self.open_interaction_frame_btn.place(x=400/2 - open_interaction_frame_btn_size/2, y=180)
        self.open_interaction_frame_btn.configure(takefocus=1)  # to add focus on the button
        self.open_interaction_frame_btn.bind("<Return>", lambda x: self.open_interaction_frame())

        self.exit_btn = ttk.Button(self.frame_use_app, text="Exit the program", command=self.quit)  # close the app
        exit_btn_size = int(self.exit_btn.winfo_reqwidth())
        self.exit_btn.place(x=400/2-exit_btn_size/2,y=220)
        self.exit_btn.bind("<Return>", lambda x: self.quit())


    def open_interaction_frame(self):
        # precondition : NONE
        # postcondition 1 : this class's frame is not placed in the main window anymore
        # postcondition 2 : an instance of InteractionInterface class is created with master and the way of
                            # using the program as as an attribute

        if tk.messagebox.askyesno("Note","Are you sure?"):
            self.frame_use_app.place_forget()  # remove the frame
            InteractionInterface(self.master, self.char_representing_selected_way.get())
            # create an InteractionInterface instance
        else:
            pass

