from tkinter import *

win = Tk()
win.geometry("600x400")

Label(win , text="Testing").pack()
canva = Frame(win , width=400 , height=400 , bd=3 , relief=RIDGE)
frame = Canvas(canva , scrollregion=(0,0,1500,1500))
frame.pack(side = "left")

for i in range(50) :
    Label(frame , text=f"hi{i}").pack()

myScrollBar = Scrollbar(canva,orient="vertical",command=frame.yview)
myScrollBar.pack(side ="right", fill = "y" )

frame.configure(yscrollcommand=myScrollBar.set)
canva.pack()

win.mainloop()