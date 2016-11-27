from Interface_LMath_with_Knowla.MainInterface import MainInterface
import tkinter as tk

__author__ = 'Ismail'


def main():
    root = tk.Tk()  # create an instance of Tk class
    MainInterface(root)  # create an instance of MainInterface cla ss
    root.mainloop()  # the interface is running in a loop

if __name__ == '__main__':
    main()  # here the program starts
