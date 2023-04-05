# author: Ugonna Ezeokoli
# date: March 14, 2023
# file: game.py a Python program that replicates the fifteen puzzle game with a GUI visual
# input: Takes in GUI which is responsible for the display of the game and inputs the object Fifteen to operate the mechanics of the game
# output: Displays the game board and functions with buttons. Also displays the evaluation of the expression entered

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen

# This function creates a button makes the text the value given. If value is 0 text will be empty
def addButton(gui, value):
    if value == 0:
        return Button(gui, text="", font=f ,height=4, width=9, bg='bisque', fg = 'black', command = lambda: clickButton(value))
    return Button(gui, text=value, font=f ,height=4, width=9, bg='brown', fg = 'black', command = lambda: clickButton(value))

# This function occurs everytime user clicks a button and it updates the board if the move is valid
def clickButton(value):
    game.update(value)
    board(gui)     #recreates board after game updated 

# This function creates the whole board by adding a button for each value in tile list.
def board(gui):
    for ind, value in enumerate(game.tiles):
        addButton(gui, value).grid(row= ind//4,column= ind % game.size,columnspan = 1)
    gui.title("Fifteen Puzzle")     #creates name of GUI window

# This function will occur when shuffle button is clicked and will make random movements to shuffle board
def shuffle(event):
    game.shuffle(100)
    board(gui)  #recreates board after game shuffled
    

    
# make a GUI window
game = Fifteen()
gui = Tk()
shuffle_button = Button(gui, text = "Shuffle")
shuffle_button.grid(row=4, column=1, columnspan=2)
shuffle_button.bind("<Button-1>",shuffle)
message = StringVar()
message.set('Click me')
f = font.Font(family='Helveca', size='12', weight='bold')
board(gui)

mainloop()