#
# An Connect Four AI Player class
#

from player import Player
from board import Board
import random

class AIPlayer(Player):
    '''A more “intelligent” computer player that uses techniques
       from AI to choose its next move.
    '''
    def __init__(self, checker, tiebreak, lookahead):
        '''Constructs a new AIPlayer object with three attributes
        '''
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        Player.__init__(self, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __str__(self):
        '''Returns a string representing an AIPlayer object.
        '''
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + \
               str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        '''Takes a list scores containing a score for each column of the board, and
           that returns the index of the column with the maximum score.
        '''
        maxi = max(scores)
        lst = [i for i in range(len(scores)) if scores[i] == maxi]
        if self.tiebreak == 'LEFT':
            return lst[0]
        elif self.tiebreak == 'RIGHT':
            return lst[-1]
        else:
            return random.choice(lst)

    def scores_for(self, board):
        '''Takes a Board object board and determines the called AIPlayer‘s scores
           for the columns in board.
        '''
        scores = [42]*board.width

        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), \
                                    self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                # print(opp_scores)
                # print(opponent.max_score_column(opp_scores))
                scores[col] = 100 - opponent.max_score_column(opp_scores)
                
                board.remove_checker(col)
            
        return scores

    def next_move(self, board):
        '''Return the called AIPlayer‘s judgment of its best possible move.
        '''
        self.num_moves += 1

        return self.max_score_column(self.scores_for(board))