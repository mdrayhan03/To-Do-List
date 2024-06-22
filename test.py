from tkinter import *
from tkcalendar import Calendar
from tktimepicker import AnalogPicker, AnalogThemes
from notifypy import Notify
from datetime import *

win = Tk()
win.geometry("600x400+200+200")

f = Frame(win)
fr = Frame(f)
Label(fr , text="HI").pack()
# print(win.winfo_screenwidth() , win.winfo_screenheight())
cal = Calendar(fr, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
 
cal.pack(pady = 20)
 
def grad_date():
    print(cal.get_date())
 
# Add Button and Label
Button(fr, text = "Get Date",
       command = grad_date).pack(pady = 20)

notification = Notify()
notification.title = "Cool Title"
notification.message = "Even cooler message."
# notification.send()
now = datetime.now()
print(date.today() , datetime.now().strftime("%H:%M"))

time_picker = AnalogPicker(fr)
time_picker.pack(expand=True, fill="both")

theme = AnalogThemes(time_picker)
theme.setNavyBlue()

fr.pack()
f.pack()
win.mainloop()