class Board:
    '''a class board that makes the object of the board for the game'''

    def __init__(self, rows, cols):
        '''this method is the constructor of the class it gives the object the following attributes:
        number of rows, number of columns, and a list of cells'''
        self.__rows = rows
        self.__cols = cols
        self.__cells = self.init_board_cells()

    def init_board_cells(self):
        '''this method creates a list of lists that has all the cells on the board'''
        cells = []
        for row in range(self.__rows):
            cells.append([])
            for col in range(self.__cols):
                cells[row].append(" ")
        return cells

    def __repr__(self):
        '''this method returns a string that represets the board'''
        board_str = ""
        for line in self.__cells:
            board_str += str(line)
            board_str += "\n"
        return board_str

    def get_empty_row(self, col):
        '''this method recieves a column and returns the the lowest row that is empty'''
        for i in range(self.__rows,0,-1):
            if self.__cells[i-1][col] == " ":
                return i-1
        return

    def insert_disc(self,row,col,disc_color):
        '''this method inserts a disc on a given cell'''
        self.__cells[row][col] = str(disc_color)

    def get_cells(self):
        '''this method returns all a list of lists that contains the cells of the board'''
        return self.__cells

    def empty_cells(self):
        '''this method returns True if all the cells are empty and False if not'''
        for i in range(self.__rows):
            for j in range(self.__cols):
                if  self.__cells[i][j] == ' ':
                    return False
        return True

    def make_column(self,column):
        '''this method makes a string of a column from the board'''
        board = ''
        for j in range(self.__rows):
            board += str(self.__cells[j][column])
        return board

    def make_row(self,row):
        '''this method makes a string of a row from the board'''
        board = ''
        for j in range(self.__cols):
            board += str(self.__cells[row][j])
        return board

    def make_diag_left_up(self,row,col):
        '''this method makes a string of the left up down diagonal on the board that contains the given coordinate and
          returns a list of the coordinates'''
        i = row - 1
        j = col - 1
        lst =[]
        board = ''
        while i>=0 and j>=0: #add all cells on the diagonale that are above and left to the given cell
            board += str(self.__cells[i][j])
            lst.append((i,j))
            i -= 1
            j -= 1
        board = board[::-1]
        lst = lst[::-1]
        while row<self.__rows and col< self.__cols:  #add all cells on the diagonale that are below and right
            board += str(self.__cells[row][col])
            lst.append((row, col))
            row += 1
            col += 1
        return board,lst

    def make_diag_left_down(self,row,col):
        '''this method makes a string of the left down up diagonal on the board that contains the given coordinate and
                  returns a list of the coordinates'''
        i = row - 1
        j = col + 1
        lst =[]
        board = ''
        while i>=0 and j<self.__cols: #add all cells on the diagonale that are above and right to the given cell
            board += str(self.__cells[i][j])
            lst.append((i,j))
            i -= 1
            j += 1
        board = board[::-1]
        lst = lst[::-1]
        while row<self.__rows and col>=0: #add all cells on the diagonale that are below and left
            board += str(self.__cells[row][col])
            lst.append((row, col))
            row += 1
            col -= 1
        return board,lst