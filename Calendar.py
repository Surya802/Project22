from tkinter import *
import calendar

root = Tk()
root.title("Calendar")
root.geometry("240x200")
root.resizable(0,0)

def show():
    a = int(y1.get())
    b = int(y2.get()) 

    cal = calendar.month(b,a)

    txt.delete(0.0,END)
    txt.insert(INSERT,cal)    

x1 = Label(root,text = "Month",font =('arial',9,'bold')).place(x=15,y=0)
x2 = Label(root,text = "Year",font =('arial',9,'bold')).place(x=115,y=0)  

y1 = Spinbox(root, values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
y1.place(x=60,y=0)
y2 = Spinbox(root,from_=1950,to_=2000,width=4)
y2.place(x=150,y=0)

btn = Button(root,text="Show",font=('arial',9,'bold'),command=show).place(x=100,y=30)

txt = Text(root,width = 24,height=8)
txt.place(x=20,y=57)

root.mainloop()
