from tkinter import *
from tkcalendar import Calendar

class Add :
    def __init__(self , window) :
        self.main_frame = Frame(window)
        self.first_frame()
        self.second_frame()
        self.main_frame.pack()
    
    def first_frame(self) :
        self.first = Frame(self.main_frame)
        Label(self.first , text="Add To-Do" , font=("Roman" , 32)).pack(pady=20)
        self.first.pack()
    
    def second_frame(self) :
        self.second = Frame(self.main_frame)
        Label(self.second , text="Title" , font=("Roman" , 18)).grid(column=0 , row=0 , sticky="w" , pady=5)
        self.title = Entry(self.second , width=30 , font=("Roman" , 18)).grid(column=1 , row=0 , sticky="w" , pady=5)
        Label(self.second , text="Description" , font=("Roman" , 18)).grid(column=0 , row=1 , sticky="w" , pady=5)
        self.des = Text(self.second , width=30 , height=3 , font=("Roman" , 18)).grid(column=1 , row=1 , sticky="w" , pady=5)
        Label(self.second , text="Date" , font=("Roman" , 18)).grid(column=0 , row=2 , sticky="w" , pady=5)
        Button(self.second , text="Calender" , width=10 , font=("Roman" , 18) , border=0 , command=self.calender).grid(column=1 , row=2 , sticky="e" , pady=5)
        Button(self.second , text="Add" , width=10 , font=("Roman" , 18) , background="#06D001").grid(column=1 , row=3 , sticky="e" , pady=5)
        self.second.pack()
    
    def calender(self) :
        self.cal = Toplevel(self.second)
        self.cal.title("Date")
        cale = Calendar(self.cal, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
 
        cale.pack(pady = 20)

        Button(self.cal , text="Set" , background="#06D001" , font=("Roman" , 18) , width=10 , command=self.top).pack(anchor="e" , padx=10 , pady=10)

    def top(self) :
        self.cal.destroy()