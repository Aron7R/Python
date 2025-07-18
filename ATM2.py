from tkinter import *

screen = Tk()
screen.title("Icon ATM")
screen.config(bg="lightblue")
screen.geometry("500x500")

balance = 0
amount_text = Label(screen,text=balance,fg="black",bg="lightblue",font=("Arial",30,"bold"))
amount_text.pack(pady=5)

#Entry
amount = Entry(screen,font=("Arial",15,"bold"),relief="solid",border=2,justify="center",width=10)
amount.pack(pady=5)

#Add Amont
deposit = Button(screen,text="Deposit",font=("Arial",13,"bold"),pady=2,padx=8,bg="blue",fg="white")
deposit.pack(pady=5)

withdraw = Button(screen,text="Withdraw",font=("Arial",13,"bold"),pady=2,padx=8,bg="blue",fg="white")
withdraw .pack(pady=5)

check = Button(screen,text="Check Balance",font=("Arial",13,"bold"),pady=2,padx=8,bg="blue",fg="white")
check.pack(pady=5)












screen.mainloop()