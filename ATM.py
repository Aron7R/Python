from tkinter import *
from tkinter import messagebox , simpledialog

Screen = Tk()
Screen.config(bg="lightblue")
Screen.title("Bangladesh National Bank")
Screen.geometry("400x400")

#Title
title = Label(Screen,text="Welcome to BNB ATM",font=("Arial",20,"bold"),bg="lightblue",fg="black")
title.pack(pady=5)

#instruction
ins = Label(Screen,text="Enter 4 digit pin",font=("Arial",15,"bold"),bg="lightblue",fg="black")
ins.pack(pady=5)

#pin
pin = Entry(Screen,width=15,font=("Arial",18,"bold"),justify="center",relief="solid")
pin.pack(pady=5)
user_pin = {
"1234":"Aron",
"2345":"Pariza",
"3456":"Codingal"
}

def Check():
my_pin = pin.get()
name = user_pin.get(my_pin)

if(name!=None):
welcome.config(text=f"Welcome {name}",fg="green")
else:
welcome.config(text=f"User Not Found",fg="red")

#Check
Enter = Button(Screen,text="Enter",bg="blue",fg="white",padx=6,pady=2,font=("Arial",12,"bold"),command=Check)
Enter.pack(pady=5)

#Result
welcome = Label(Screen,font=("Arial",18,"bold"),bg="lightblue")
welcome.pack(pady=5)

Screen.mainloop()