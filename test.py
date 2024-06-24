from tkinter import *
from tkcalendar import Calendar
from tktimepicker import AnalogPicker, AnalogThemes
from notifypy import Notify
from datetime import *

win = Tk()
win.geometry("600x400+200+200")

# f = Frame(win)
# # scrollbar = Scrollbar(f)
# # scrollbar.pack( side = RIGHT, fill=Y )
# fr = Frame(f)
# Label(fr , text="HI").pack()
# # print(win.winfo_screenwidth() , win.winfo_screenheight())
# # cal = Calendar(fr, selectmode = 'day',
# #                year = 2020, month = 5,
# #                day = 22)
 
# # cal.pack(pady = 20)
 
# # def grad_date():
# #     print(cal.get_date())
 
# # Add Button and Label
# Button(fr, text = "Get Date").pack(pady = 20)

# notification = Notify()
# notification.title = "Cool Title"
# notification.message = "Even cooler message."
# # notification.send()
# now = datetime.now()
# print(date.today() , datetime.now().strftime("%H:%M"))

# time_picker = AnalogPicker(fr)
# time_picker.pack(expand=True, fill="both")

# theme = AnalogThemes(time_picker)
# theme.setNavyBlue()

# fr.pack()
# # scrollbar.config( command = fr.yview)
# f.pack()
scrollbar = Scrollbar(win)
scrollbar.pack( side = RIGHT, fill=Y )
c = Canvas(win , width=600 , height=400 , border=2 , relief="solid" , yscrollcommand=scrollbar.set)
for i in range(50) :
    Label(c , text=i).pack()
    Button(c , text = "Press").pack()
c.pack()
scrollbar.config(command = c.yview)
win.mainloop()