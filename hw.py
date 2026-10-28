#Coin Toss
from tkinter import *
import tkinter.font as font
import random

#Set up
root = Tk()
root.geometry("700x300")
root.title("Coin Toss")

#Variables
heads_count = 0
tails_count = 0

#Options - Label
options = Label(root, text = "Heads or Tails?", font = ("Times New Roman", 20, "normal"), fg = "black")
options.pack(pady = 10)

#Sides - List
sides = [("Heads"), ("Tails")]

#Coin - function
def coin():
    side = random.choice(sides)

    #Winner Message - Label
    winner_message = Label(root, text = ("Its " + str(side)), font = font.Font(size = 14), fg = "blue")
    winner_message.pack(pady = 10)

#Flip Coin - Button
flip_coin = Button(root, text = "Flip Coin", bg = "yellow", fg = "blue", width = 15, pady = 5, command = coin)
flip_coin.pack(pady = 10)

root.mainloop()