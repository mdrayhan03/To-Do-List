from tkinter import *

class List :
    def __init__(self , window) :
        self.main_frame = Frame(window , width=600 , height=400)
        self.first_frame()
        self.second_frame()
        self.main_frame.pack()
    
    def first_frame(self) :
        self.first = Frame(self.main_frame)
        Label(self.first , text="To-Do List" , font=("Roman" , 32)).pack(pady = 10)
        self.first.pack()
    
    def second_frame(self) :
        self.second = Frame(self.main_frame)
        self.scrollbar = Scrollbar(self.second)
        self.scrollbar.pack( side = RIGHT, fill=Y )
        mylist = Listbox(self.second, yscrollcommand = self.scrollbar.set , width = 600 , height = 200 , borderwidth = 0 , background="#F0F0F0")  #by default bg color of tkinter is #F0F0F0
        for line in range(100):
            mylist.insert(END, "This is line number " + str(line))
   
        mylist.pack( side = LEFT, fill = BOTH )
        self.scrollbar.config( command = mylist.yview )
        self.second.pack()