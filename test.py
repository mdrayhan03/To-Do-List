# from tkinter import *
# from tkcalendar import Calendar
# from tktimepicker import AnalogPicker, AnalogThemes
# from notifypy import Notify
# from datetime import *

# win = Tk()
# win.geometry("600x400+200+200")

# # f = Frame(win)
# # # scrollbar = Scrollbar(f)
# # # scrollbar.pack( side = RIGHT, fill=Y )
# # fr = Frame(f)
# # Label(fr , text="HI").pack()
# # # print(win.winfo_screenwidth() , win.winfo_screenheight())
# # # cal = Calendar(fr, selectmode = 'day',
# # #                year = 2020, month = 5,
# # #                day = 22)
 
# # # cal.pack(pady = 20)
 
# # # def grad_date():
# # #     print(cal.get_date())
 
# # # Add Button and Label
# # Button(fr, text = "Get Date").pack(pady = 20)

# # notification = Notify()
# # notification.title = "Cool Title"
# # notification.message = "Even cooler message."
# # # notification.send()
# # now = datetime.now()
# # print(date.today() , datetime.now().strftime("%H:%M"))

# # time_picker = AnalogPicker(fr)
# # time_picker.pack(expand=True, fill="both")

# # theme = AnalogThemes(time_picker)
# # theme.setNavyBlue()

# # fr.pack()
# # # scrollbar.config( command = fr.yview)
# # f.pack()
# # scrollbar = Scrollbar(win)
# # scrollbar.pack( side = RIGHT, fill=Y )
# # c = Canvas(win , width=600 , height=400 , border=2 , relief="solid" , yscrollcommand=scrollbar.set)
# # for i in range(50) :
# #     Label(c , text=i).pack()
# #     Button(c , text = "Press").pack()
# # c.pack()
# # scrollbar.config(command = c.yview)
# Label(win , text="one").grid(column=1 , row=8)
# Label(win , text="two").grid(column=8 , row=1)
# win.mainloop()

import customtkinter as ctk
from tkinter import *

def add_todo():
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()
    entry.delete(0, ctk.END)

root = Tk()
root.geometry("750x450")
root.title("Todo App")

title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
entry.pack(fill="x")

add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
add_button.pack(pady=20)

root.mainloop()