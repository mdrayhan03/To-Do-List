from tkinter import *

win = Tk()
win.geometry("600x400+200+200")

f = Frame(win)
fr = Frame(f)
Label(fr , text="HI").pack()
print(win.winfo_screenwidth() , win.winfo_screenheight())
fr.pack()
f.pack()
win.mainloop()