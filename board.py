#
# A Connect Four Board class
#

class Board:
    '''A data type for a Connect Four board with arbitrary dimensions
    '''

    def __init__(self, height, width):
        '''A constructor for Board objects
        '''
        self.height = height
        self.width = width
        self.slots = [[' ']*width for row in range(height)]

    def __str__(self):
        '''Returns a string representation of a Board
        '''
        s = ''

        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        for row in range(1):
            for col in range((self.width*2)+1):
                s += '-'
            s += '\n'
        for row in range(1):
            s += ' '
            for col in range(self.width):
                s += str(col % 10) + ' ' 

        return s
        
    def __repr__(self):
        '''Returns string representing the called Board object'''
        return str(self)

    def add_checker(self, checker, col):
        '''Adds the checker, either X or O, into the appropriate row
           in column col of the board
        '''
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        row = 0
        
        while self.slots[row][col] == ' ':
            row += 1
            if row > self.height - 1:
                break
 
        self.slots[row-1][col] = checker

    def clear(self):
        '''Clear the Board object on which it is called by setting
           all slots to contain a space character
        '''
        self.__init__(self.height, self.width)
        self.__str__()
        self.__repr__()

    def add_checkers(self, colnums):
        '''Takes in a string of column numbers and places alternating
           checkers in those columns of the called Board object, 
           starting with 'X'.
        '''
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
    
    def can_add_to(self, col):
        '''Returns True if it is valid to place a checker in the column col
           on the calling Board object. Otherwise, return False.
        '''
        if col < 0 or col > self.width - 1:
            return False
        elif self.slots[0][col] == ' ':
            return True
        else:
            return False

    def is_full(self):
        '''Returns True if the called Board object is completely full of
           checkers, and returns False otherwise.
        '''
        count = 0
        
        for i in range(self.width):
            if self.can_add_to(i) == False:
                count += 1
            
        if count == self.width:
            return True
        else:
            return False

    def remove_checker(self, col):
        '''Removes the top checker from column col of the called Board object.
           If the column is empty, then the method should do nothing.
        '''
        assert(col >= 0 and col < self.width)

        row = 0
        
        while self.slots[row][col] == ' ':
            row += 1
            if row > self.height - 1:
                break
            
        if row < self.height:
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        return False

    def is_vertical_win(self, checker):
        '''Checks for a vertical win for the specified checker.
        '''
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        return False

    def is_down_diagonal_win(self, checker):
        '''Checks for a vertical win for the specified checker.
        '''
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True

        return False

    def is_up_diagonal_win(self, checker):
        '''Checks for a vertical win for the specified checker.
        '''
        
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True

        return False

    def is_win_for(self, checker):
        '''Accepts a parameter checker that is either 'X' or 'O', and returns
           True if there are four consecutive slots containing checker on the
           board. Otherwise, it should return False.
        '''
        assert(checker == 'X' or checker == 'O')
        
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False




        
