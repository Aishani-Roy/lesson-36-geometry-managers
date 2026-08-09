from tkinter import *
from datetime import date
root =Tk()
root.geometry('400x300')

lbl=Label(text="hey guys!",fg="white",bg="blue",height=1,width=40)
name_lbl=Label(text="Full Name",bg="purple")
name_entry=Entry()

def display():
    name=name_entry.get()
    global message
    message="welcome to the app!\ntodays date is:"
    greet="hello "+name+"\n"
    textb.insert(END,greet)
    textb.insert(END,message)
    textb.insert(END,date.today())

textb=Text(height=3,width=40)
btn=Button(text="Begin",command=display,height=1,bg="green",fg="white")

lbl.place(x=50,y=50)
name_lbl.place(x=50,y=100)
name_entry.place(x=150,y=100)
btn.place(x=150,y=150)
textb.place(x=50,y=200)

root.mainloop()
    