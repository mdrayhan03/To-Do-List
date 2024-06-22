from tkinter import *
import List_File 
import time 

class MainApplication :
    def __init__(self) :
        self.window = Tk()
        self.window.geometry("600x400+200+200")
        self.window.resizable(False , False)
        self.window.title("To-Do List")
        List_File.List(self.window)
        self.window.mainloop()
    

MainApplication()