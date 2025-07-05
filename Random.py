from tkinter import *
import random

screen = Tk()
screen.title("Number Game")
screen.geometry("350x350")
screen.config(bg="lightblue")

heading = Label(screen,text="Let's Play Number Game",bg="blue",fg="white",font=("Ariel",15,"bold"),borderwidth=2,)
heading.pack(pady=5)

rule = Label(screen,text="-Rule-\nComputer must choose a \nrandom number between 1-10.\nYou have to guess the Number",
bg="lightblue",fg="black",font=("Arial",10,"bold"),borderwidth=2,)
rule.pack(pady=3)

number_box = Entry(screen,font=("Arial",10,"bold"))
number_box.pack(pady=3,padx=5)

random_number = random.randint(1,10)
def Play():
    user_number = int(number_box.get())
    if(user_number==random_number):
        result.config(text="You Won",fg="green")
    elif (user_number>random_number):
        result.config(text="Please try lower number",fg="red")
    elif (user_number<random_number):
        result.config(text="Please try higher number",fg="red")
    else:
        result.config(text="Invalid Entry",fg="red")


guess = Button(screen,text="Guess",bg="crimson",fg="white",border=2,font=("Arial",10,"bold"),padx=5,pady=2,command=Play)
guess.pack(padx=5,pady=2)

result = Label(screen,font=("Arial",15,"bold"),bg="lightblue")
result.pack(pady=3)

screen.mainloop()