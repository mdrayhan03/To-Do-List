from tkinter import *
from tkcalendar import Calendar

class List :
    def __init__(self , window) :
        self.main_frame = Frame(window , width=600 , height=400)
        self.first_frame()
        self.second_frame()
        self.main_frame.pack()
    
    def first_frame(self) :
        self.first = Frame(self.main_frame)
        Label(self.first , text="To-Do List" , font=("Roman" , 32)).pack(pady = 10)
        # self.cal = Calendar(self.first, selectmode = 'day')
 
        # self.cal.pack(pady = 20)
        # b = Button(self.first , text="Date" , command="self.DateClick")
        # b.pack()
        self.first.pack()
    
    def second_frame(self) :
        self.second = Frame(self.main_frame)
        for i in range(50) :
            self.makeInstance()
        # self.scrollbar = Scrollbar(self.second)
        # self.scrollbar.pack( side = RIGHT, fill=Y )
        # mylist = Listbox(self.second, yscrollcommand = self.scrollbar.set , width = 600 , height = 200 , borderwidth = 0 , background="#F0F0F0")  #by default bg color of tkinter is #F0F0F0
        # for line in range(100):
        #     mylist.insert(END, "This is line number " + str(line))
   
        # mylist.pack( side = LEFT, fill = BOTH )
        # self.scrollbar.config( command = mylist.yview )
        self.second.pack()

    def DateClick(self) :
        print(self.cal.get_date())

    def makeInstance(self) :
        self.new = Frame(self.second)
        Label(self.new , text="HI").pack()
        self.new.pack()