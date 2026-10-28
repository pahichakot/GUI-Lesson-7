#Die Roller
from tkinter import *
import random

#Set up
root = Tk()
root.geometry("500x700")
root.title("Die Roller")

#Directions - Label
directions = Label(root, text = "Roll the Die!", font = ("Times New Roman", 20, "normal"), fg = "black")
directions.pack(pady = 10)

#Nums - List
nums = [("1"), ("2"), ("3"), ("4"), ("5"), ("6")]

#Coin - function
def number():
    num = random.choice(nums)

    #Winner Message - Label
    if str(num) != "6":
        winner_message = Label(root, text = str(num), font = ("Times New Roman", 40, "normal"), fg = "blue")
        winner_message.pack(pady = 10)

    elif str(num) == "6":
        winner_message = Label(root, text = str(num), font = ("Times New Roman", 40, "normal"), fg = "red")
        winner_message.pack(pady = 10)

#Roll Die - Button
roll_die = Button(root, text = "Roll Die", bg = "light pink", fg = "purple", width = 15, pady = 5, command = number)
roll_die.pack(pady = 10)

root.mainloop()