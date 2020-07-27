import math
def solve_sudoku(board):
    '''this function solves a sudoku board'''
    new_board = board[:]
    if solve_sudoku_helper(new_board):
        return True
    else:
        return False

def solve_sudoku_helper(board):
    '''this function solves a sudoku board returns true if the board can be solved
    and false if not'''
    pointer = [0, 0]
    if not find_empty_location(board, pointer): #looks for an empty spot on the board
        return True
    row = pointer[0]
    col = pointer[1]
    for num in range(1, len(board)+1):
        if legal_placement(num,row,col,board): #checks if number can be put in empty spot
            board[row][col] = num
            if solve_sudoku_helper(board):
                return True
            board[row][col] = 0
    return False

def legal_placement(num,row,col,board):
    '''this function checks if the number given can be put in the given placement'''
    root_n = math.sqrt(len(board))
    if (check_num_in_square(num,row,col,board,root_n) or check_num_in_col(num,row,col,board)
            or num in board[row][0:col] or num in board[row][col+1:]):
        return False
    return True

def check_num_in_square(num,row,col,board,root_n):
    '''this function returns a list of all numbers inside a square'''
    square_start_row = int((row//root_n)*root_n)
    square_start_col = int((col // root_n) * root_n)
    for i in range(square_start_row,square_start_row+int(root_n)):
        for j in range(square_start_col,square_start_col+int(root_n)):
            if num==board[i][j]:
                return True
    return False

def check_num_in_col(num,row,col,board):
    '''this function returns a list with all the numbers that appear in the given column'''
    for row in range(0,row): #checks if the num is inside the row from the start to the index of the spot
            if num == board[row][col]:
                return True
    for row in range(row+1,len(board)): #checks if the num is inside the row from the spot to the end
            if num == board[row][col]:
                return True
    return False

def find_empty_location(board, pointer):
    '''this function finds an empty index inside the board'''
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                pointer[0] = row
                pointer[1] = col
                return True
    return False

def print_k_subsets(n,k):
    '''this function prints all sub groups size k from 0 to n-1'''
    lst=list(range(n))
    if n==0:
        return
    pointer=''
    if k<=n:
        print_k_subsets_helper(lst, k,pointer)

def print_k_subsets_helper(lst,k,pointer):
    '''this function prints all sub groups size k from 0 to n-1'''
    if k == 0:
        for i in range(len(pointer)-1):
            if pointer[i]>pointer[i+1]:
                return
        print(make_lst_from_string(pointer))
        return
    for i in lst:
        if str(i) in pointer:
            continue
        new_pointer=pointer+str(i)
        print_k_subsets_helper(lst,k-1, new_pointer)

def make_lst_from_string(pointer):
    '''this function recieves a string and returns a list of all subgroups'''
    lst = []
    for i in range(len(pointer)):
        lst.append(int(pointer[i]))
    return lst

def fill_k_subsets(n,k,lst):
    '''this function makes a list with all sub groups size k from 0 to n-1'''
    lst_n = list(range(n))
    pointer = ''
    if k<=n:
        fill_k_subsets_helper(lst_n, k, pointer,lst)

def fill_k_subsets_helper(lst_n,k,pointer,lst):
    '''this function makes a list with all sub groups size k from 0 to n-1'''
    if k == 0:
        for i in range(len(pointer)-1):
            if pointer[i]>pointer[i+1]:
                return
        temp_lst = []
        for i in range(len(pointer)):
            temp_lst.append(int(pointer[i]))
        lst.append(temp_lst)
        return
    for i in lst_n:
        if str(i) in pointer:
            continue
        new_pointer=pointer+str(i)
        fill_k_subsets_helper(lst_n,k-1, new_pointer,lst)

def return_k_subsets(n,k):
    '''this function gets a list and returns a new list with all sub groups size k from 0 to n-1'''
    new_lst=[]
    if n==0:
        return new_lst
    if k <= n:
        main_lst=return_k_subsets_helper(n, k)
        for i in main_lst:
            if len(i) != k: #checks if all groups are size k
                continue
            new_lst.append(i)
    return new_lst

def return_k_subsets_helper(n,k):
    '''this function makes a list of sub groups from 0 to n-1'''
    if k == 0:
        return [[]]
    main_lst=[]
    for i in range(n):
        temp_lst=return_k_subsets_helper(n, k-1)
        for lst in temp_lst:
                if lst==[]:
                    lst.append(i)
                if i in lst or lst[len(lst)-1]>i:
                    continue
                lst.append(i)
        main_lst.extend(temp_lst)
    return main_lst

