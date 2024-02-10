from tkinter import *
from tkcalendar import *

window=Tk()
window.title('pick the date')
window.geometry('500x400')
window.configure(bg='light blue')

cal=Calendar(window,selectmode='day')
cal.pack()

def grab_date():
    l1.config(text=cal.get_date(),fg="#a52a2a",bg="#ffe4c4",font=("calibri",20))

b1=Button(window,text='Select the Date',command=grab_date,bg="grey",fg="black",bd=4,font=('Helvetica',20))
b1.pack()
l1=Label(window,text='',bg='light blue')
l1.pack()
window.mainloop()
