from tkinter import *
from tkinter import ttk
from Interface_LMath_with_Knowla.UseAppInterface import UseAppInterface

__author__ = 'Ismail Zobui'


class MainInterface(Frame):
    def __init__(self, master):  # the class attributes.
        Frame.__init__(self, master)
        #  the class instance has an attribute of the master ( the root from the main function)
        master.title("Learn Math with Knowla")  # set a title for the window
        master.geometry("700x500+300+100")  # set a size for the window
        self.create_widgets()  # call this function

    def create_widgets(self):

        # precondition : none
        # postcondition : widgets are created

        self.main_btn = ttk.Button(self.master,text ="main", command=self.go_to_main)  # go to the main interface
        self.main_btn.place(x=0,y=0)
        self.main_btn.bind("<Return>", lambda x: self.go_to_main())

        self.exit_btn_master = ttk.Button (self.master, text="exit", command=self.quit)  # button to quit the program.
        self.exit_btn_master.place(x=80,y=0)
        self.exit_btn_master.bind("<Return>", lambda x: self.quit())

        self.mainframe = Frame(self.master, width=300, height=200)  # create a frame inside the master
        self.mainframe['relief'] = 'sunken'
        self.mainframe['borderwidth'] = 2
        self.mainframe.place(x=700/2-300/2, y=500/2-200/2)  # place the frame in these coordination

        self.welcome_label = ttk.Label(self.mainframe, text="Welcome to Learn Math with Knowla")
        # create a label inside the mainframe
        welcome_label_size = int(self.welcome_label.winfo_reqwidth())  # get the label size
        self.welcome_label.place(x=300/2-welcome_label_size/2 ,y=40)

        self.enter_btn = ttk.Button(self.mainframe, text="Click Here to Begin",
                                    command=self.open_use_app_interface_frame)  # to go to the next frame
        # create a button inside the mainframe
        enter_btn_size = int(self.enter_btn.winfo_reqwidth())
        self.enter_btn.place(x=300/2-enter_btn_size/2,y=70)
        self.enter_btn.focus_set()  # to add focus on the button
        self.enter_btn.bind("<Return>", lambda x: self.open_use_app_interface_frame())

        self.exit_btn = ttk.Button(self.mainframe, text="Exit", command=self.quit)
        # create a button inside the main frame, its command to exit the program.
        exit_btn_size = int(self.exit_btn.winfo_reqwidth())
        self.exit_btn.place(x=300/2-exit_btn_size/2,y=100)
        self.exit_btn.bind("<Return>", lambda x: self.quit())

    def open_use_app_interface_frame(self):  # to go to the next frame
        self.mainframe.place_forget()  # remove the mainframe
        UseAppInterface(self.master)  # create an instance of UseAppInterface and send it the master attribute

    def go_to_main(self):  # to go to the main window
        for widgets in self.master.winfo_children():
            widgets.destroy()
        self.master.title("Learn Math with Knowla")  # set a title for the window
        self.create_widgets()



