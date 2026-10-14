#Rock Paper Scissors Game
from tkinter import *
import tkinter.font as font
import random

#Set up
root = Tk()
root.geometry("700x300")
root.title("Rock, Paper, Scissors Game")

#Variables
app_font = font.Font(size = 12)
player_score = 0
computer_score = 0

#List of options for computer
options = [("rock", 0), ("paper", 1), ("scissors", 2)]

#Computer wins - Function
def computer_wins():
    global player_score, computer_score
    computer_score = computer_score + 1
    winner_message.config(text = "Computer Wins ! ")

    computer_score_label.config(text = "Computer Score : " + str(computer_score))
    user_score_label.config(text = "Your Score : " + str(player_score))

#User wins - Function
def user_wins():
    global player_score, computer_score
    player_score = player_score + 1
    winner_message.config(text = "User Wins ! ")

    user_score_label.config(text = "Your Score : " + str(player_score))
    computer_score_label.config(text = "Computer Score : " + str(computer_score))

#Tie - Function
def tie():
    global player_score, computer_score
    winner_message.config(text = "Tie ! Neither won...")

    user_score_label.config(text = "Your Score : " + str(player_score))
    computer_score_label.config(text = "Computer Score : " + str(computer_score))

#Let computer select option randomly - Function
def get_computer_choice():
    return random.choice(options)

#Let player select option
def get_user_choice(player_input):
    global computer_score, player_score
    
    computer_input = get_computer_choice()




#Title - Label
game_title = Label(root, text = "Rock, Paper, Scissors, SHOOT !", font = font.Font(size = 20), fg = "grey")
game_title.pack()

#Winner Message - Label
winner_message = Label(root, text = "Let's start the game !", font = font.Font(size = 14), fg = "green")
winner_message.pack(pady = 10)

#Create bottom frame
frame = Frame(root)
frame.pack()

#User options - Label
user_options = Label(frame, text = "Your Options", font = app_font, fg = "purple")
user_options.grid(row = 0, column = 0)

#Rock - Button
rock_btn = Button(frame, text = "Rock", bg = "pink", width = 15, pady = 5)
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

#Paper - Button
paper_btn = Button(frame, text = "Paper", bg = "silver", width = 15, pady = 5)
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

#Scissors
scissors_btn = Button(frame, text = "Scissors", bg = "light blue", width = 15, pady = 5)
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

#Score - Label
score_label = Label(frame, text = "Score", font = app_font, fg = "purple")
score_label.grid(row = 2, column = 0)

#User selection - Label
user_selection = Label(frame, text = "You Selected : ", font = app_font, fg = "black")
user_selection.grid(row = 3, column = 1, pady = 5)

#Computer selection - Label
computer_selection = Label(frame, text = "Computer Selected : ", font = app_font, fg = "red")
computer_selection.grid(row = 3, column = 2, pady = 5)

#User score - Label
user_score_label = Label(frame, text = "Your Score : ", font = app_font, fg = "black")
user_score_label.grid(row = 4, column = 1, pady = 5, padx = 5)

#Computer score - Label
computer_score_label = Label(frame, text = "Computer Score : ", font = app_font, fg = "red")
computer_score_label.grid(row = 4, column = 2, pady = 5, padx = 5)

root.mainloop()