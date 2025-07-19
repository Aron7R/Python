from tkinter import *
from tkinter import messagebox

balance = 1000
pin = 1234

def show_login():
    global login_screen
    login_screen = Tk()
    login_screen.title("Welcome to BNB ATM")
    login_screen.config(bg="lightblue")
    login_screen.geometry("300x300")

    ins = Label(login_screen,text="Enter PIN",font=("Arial",18,"bold"),justify="center")
    ins.pack(pady=5)

    pin_entry = Entry(login_screen,width=15, relief="solid",font=("Arial",18,"bold"))
    pin_entry.pack(pady=5)

    def Verify_Account():
        number = int(pin_entry.get())
        if(number==pin):
            login_screen.destroy()
            show_menu()
        else:
            messagebox.showerror("ERROR","Invalid Entry")
            
    verify = Button(login_screen,text="Verify",font=("Arial",10,"bold"),fg="white",bg="green",padx=5,pady=2,command=Verify_Account)
    verify.pack(pady=5)

    login_screen.mainloop()

def show_menu():
    pass

menu_screen.mainloop()