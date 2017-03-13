#
# A Connect Four Game
#

from board import Board
from player import Player
from aiplayer import AIPlayer
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One of them uses 'X' checkers and the other uses 'O' checkers.
    """

    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board

def process_move(player, board):
    '''Takes Player object and Board object and process a single move by the
       player on the board. 
    '''
    p = player
    print(p.__str__() + "'s turn")
    col = p.next_move(board)
    board.add_checker(p.checker, col)
    print('\n')
    print(board)
    
    if board.is_win_for(p.checker):
        print('Player ' + p.checker + ' wins in ' + str(p.num_moves) + ' moves.' \
              '\n' + 'Congratulations!')
        return True
    elif board.is_full():
        print("It's a tie!")
        return True
    else:
        return False

class RandomPlayer(Player):
    '''Subclass of Player class'''
    def next_move(self, board):
        
        self.num_moves += 1
        available = []
        
        for col in range(b.width):
            if board.can_add_to(col) == True:
                available += [col]
        print(random.choice(available))
