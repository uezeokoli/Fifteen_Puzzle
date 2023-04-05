# author: Ugonna Ezeokoli
# date: March 14, 2023
# file: fifteen.py a Python program that replicates the fifteen puzzle game
# input: an object calledn Fifteen that creates a visual display for the game and has functions for the game to function
# output: outputs the board of the game and the switches that happen when a player makes a move 

import numpy as np
from random import choice

class Fifteen:
    
    # create an array of tiles
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size = 4):
        self.tiles = [i for i in range(1,size**2)] + [0]
        self.size = size


    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose
    def update(self, move):
        if self.is_valid_move(move):
            self.transpose(self.tiles.index(0),self.tiles.index(move))

    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space) 
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j):
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    # shuffles tiles by updating with random tile choices
    # steps is the number of times the board attempts to update
    def shuffle(self, steps=100):
        for i in range(steps):
            self.update(choice(self.tiles))
        
    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor
    def is_valid_move(self, move):
        # returns false if the tile is not directly touching other tile
        if (self.tiles.index(0) % self.size == 3) and (self.tiles.index(move) % self.size == 0):
            return False
        if (self.tiles.index(0) % self.size == 0) and (self.tiles.index(move) % self.size == 3):
            return False
        # if abs() is equal to 4 that means that tiles is either above or below tile 0 and if abs() equal 1 that means tiles is either left or right of tile 0
        return (abs(self.tiles.index(0)-self.tiles.index(move)) == 4) or (abs(self.tiles.index(0)-self.tiles.index(move)) == 1)
        
    # verify if the puzzle is solved
    def is_solved(self):
        return self.tiles == [i for i in range(1,self.size**2)] + [0]
    

    # draws the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
            # creates new tiles list to change 0 into a " " for the board
            tiles = []
            for num in self.tiles:
                if num == 0:    
                    tiles.append(" ")
                else:
                    tiles.append(num)
            # formats the board with a border for display
            print('+---+---+---+---+')
            print('|{:2} |{:2} |{:2} |{:2} |'.format(tiles[0], tiles[1], tiles[2], tiles[3]))
            print('+---+---+---+---+')
            print('|{:2} |{:2} |{:2} |{:2} |'.format(tiles[4], tiles[5], tiles[6], tiles[7]))
            print('+---+---+---+---+')
            print('|{:2} |{:2} |{:2} |{:2} |'.format(tiles[8], tiles[9], tiles[10], tiles[11]))
            print('+---+---+---+---+')
            print('|{:2} |{:2} |{:2} |{:2} |'.format(tiles[12], tiles[13], tiles[14], tiles[15]))
            print('+---+---+---+---+')
    

    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15 
    def __str__(self):
        # creates string varialbe to represent board
        string = ""
        # iterates through len of tiles
        for i in range(len(self.tiles)):    
            # if tile on very right, ands \n to make new line for board
            if (i+1) % self.size == 0:
                # if tile val is 0 replaces it with " "
                if self.tiles[i] == 0:
                    string += f'{" ":2} '
                    string += '\n'
                    continue
                string += f'{self.tiles[i]:2} '
                string += '\n'
            # if not on very right, doesn't add \n for a new line
            else:
                # if tile val is 0 replaces it with " "
                if self.tiles[i] == 0:
                    string += f'{" ":2} '
                    continue
                string += f'{self.tiles[i]:2} '
        return string




    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        pass

    # solve the puzzle (optional)
    def solve(self):
        pass


if __name__ == '__main__':
    
    game = Fifteen()


    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    '''You should be able to play the game if you uncomment the code below'''
    # '''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    # '''
    
    
        
