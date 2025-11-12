from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    comp_choice = random.choice(choices)
    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or (user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {comp_choice}\n{result}")

def rock():
    play("Rock")

def paper():
    play("Paper")

def scissors():
    play("Scissors")

Label(root, text="Choose Rock, Paper, or Scissors").pack(pady=10)

Button(root, text="Rock", width=10, command=rock, bg="red").pack(pady=5)
Button(root, text="Paper", width=10, command=paper, bg="red").pack(pady=5)
Button(root, text="Scissors", width=10, command=scissors, bg="red").pack(pady=5)

result_label = Label(root, text="", font=('Arial', 12))
result_label.pack(pady=20)

root.mainloop()