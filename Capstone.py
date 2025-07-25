from tkinter import *
from tkinter import messagebox
import string
import random

screen = Tk()
screen.geometry("300x300")
screen.title("Password Generatior")

Label(screen,text="Enter Password Length").pack(pady=5)

length = Entry(screen)
length.pack(pady=5)

def Generate_password():
    try:
        l = int(length.get())
        if l<=0:
            messagebox.showerror("ERROR","Password length should not be less than or equal to 0")
    except:
        messagebox.showerror("ERROR","Password length can not be alphabate")

    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(1):
        password = ''.join(random.choice(characters) for i in range(l))

    result.delete(0, END)
    result.insert(0, password)

def Copy_password():
    pass



Button(screen,text="Generate Password",command=Generate_password).pack(pady=5)

result = Entry(screen,width=30)
result.pack(pady=5)

Button(screen,text="Copy",command=Copy_password).pack (pady=5)

screen.mainloop()