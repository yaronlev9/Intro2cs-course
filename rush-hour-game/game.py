from car import Car
from board import Board
from helper import *
import sys

class Game:
    """class that makes the objects of the game with its attributes (board) that includes methods."""
    NAMES = ('Y', 'B', 'O', 'W', 'G', 'R')
    MOVES = ('u','d','l','r')
    INVALID_INPUT = 'the input is invalid'
    INVALID_MOVE  = 'move is invalid'
    WIN_MSG = 'you win!'

    def __init__(self, board):
        """Initialize a new Game object.
        param board: An object of type board"""
        self.__board=board

    def __single_turn(self):
        """ The function runs one round of the game :
            1. Get user's input of: what color car to move, and what direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input."""
        possible_moves = board.possible_moves()
        print('possible_moves: ', possible_moves)
        move = input("plz enter name of car, direction:",)
        if len(move)==3:
            name,comma,direction = move
            if name in Game.NAMES and direction in Game.MOVES and comma == ',':
                for move in possible_moves:
                    if move[0] == name and move[1] == direction:
                        board.move_car(name,direction)
                        print(self.__board)
                        return
                print(Game.INVALID_MOVE)
        else:
                print(Game.INVALID_INPUT)

    def play(self):
        """"The main driver of the Game. Manages the game until completion.
            return: None"""
        print(self.__board)
        while self.__board.cell_content(self.__board.target_location()) is None:
            self.__single_turn()
        print(Game.WIN_MSG)
        return None

if __name__== "__main__":
    board=Board()
    json = load_json(sys.argv[1])
    for key in json:
        value = json[key]
        if key in Game.NAMES and value[0]<=4 and value[0]>=2:
            car=Car(key,value[0],value[1],value[2])
            board.add_car(car)
    game=Game(board)
    game.play()
