from tkinter import *

window=Tk()

def conversion():
    #print("text")
    grams=float(e1_val.get())*1000
    t1.delete("1.0", END)
    t1.insert(END,grams)
    pounds=float(e1_val.get())*2.20462
    t2.delete("1.0", END)
    t2.insert(END,pounds)
    ounces=float(e1_val.get())*35.274
    t3.delete("1.0", END)
    t3.insert(END,ounces)

l1=Label(window,text="Kg")
l1.grid(row=0,column=0)

b1=Button(window,text="Convert",command=conversion)
b1.grid(row=0,column=2)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()
