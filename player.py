#
# A Connect Four Player class 
#

from board import Board

class Player:
    '''Represents a player of the Connect Four game 
    '''
    def __init__(self, checker):
        '''constructs a new Player object
        '''
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0
        
    def __str__(self):
        '''returns a string representing a Player object
        '''
        return 'Player ' + self.checker

    def __repr__(self):
        return str(self)
    
    def opponent_checker(self):
        '''Returns a one-character string representing the checker
           of the Player object’s opponent. 
        '''

        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        '''Accepts a Board object as a parameter and returns the column
           where the player wants to make the next move.
        '''
        self.num_moves += 1

        while True:
            col = int(input('Enter a column: '))
            if board.can_add_to(col) == True:
                return col
            else:
                print('Try again!')