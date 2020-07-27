def print_to_n(n):
    '''this function prints all ints fron 1 to n in a down order'''
    if n<1:
        return
    else:
        print_to_n(n-1)
        print(int(n))

def print_reversed(n):
    '''this function prints all ints fron n to 1 in an up order'''
    if n<1:
        return
    else:
        print(int(n))
        print_reversed(n-1)

def is_prime(n):
    '''this function checks if a number is prime'''
    i=n-1
    if n<=1:
        return False
    else:
        return has_divisor_smaller_than(n,i)

def has_divisor_smaller_than(n,i):
    '''this function checks if the 2 ints given are divided without a remainder'''
    if i==1:
        return True
    elif n%i==0:
        return False
    else:
        return not n%(i)==0 and has_divisor_smaller_than(n,i-1)

def exp_n_x(n,x):
    '''this function calculates the taylor column of exponent(x) from 0 to n'''
    i=n
    if i>=0 and type(n)==int:
        return exp_n_x_helper(x, i)

def exp_n_x_helper(x,i):
    '''this function calculates the sum of the taylor column of exponent(x)'''
    if i==0:
        return float(1)
    else:
        print((x ** i) / (factorial(i)))
        return (x**i)/(factorial(i)) + exp_n_x_helper(x, i - 1)

def factorial(n):
    '''this function calculates factorial of n'''
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def play_hanoi(hanoi,n,src,dest,temp):
    '''this function solves the game of hanoi with n disks'''
    if n<=0:
        return
    if int(n)==1:
        hanoi.move(src, dest)
        return
    play_hanoi(hanoi, n - 1,src,temp,dest)
    hanoi.move(src, dest)
    play_hanoi(hanoi, n - 1, temp, dest, src)

def print_sequences(char_list,n):
    '''this function recievs a list of chars and a number'''
    if n==0:
        return
    pointer=''
    print_sequences_helper(char_list, n, pointer)

def print_sequences_helper(char_list,n,pointer):
    '''this function prints all the words in length n with the chars in the list given'''
    if n == 0:
        print(pointer)
        return
    for i in char_list:
        new_pointer = pointer + i
        print_sequences_helper(char_list,n-1, new_pointer)

def print_no_repetition_sequences(char_list,n):
    '''this function recievs a list of chars and a number'''
    if n==0:
        return
    pointer=''
    print_no_repetition_sequences_helper(char_list,n,pointer)

def print_no_repetition_sequences_helper(char_list,n,pointer):
    '''this function prints all the words in length n with the chars in the list given
    every char is shown once in the word'''
    if n == 0:
        print(pointer)
        return
    for i in char_list:
        if i in pointer:
            continue
        new_pointer = pointer + i
        print_no_repetition_sequences_helper(char_list,n-1, new_pointer)

def parentheses(n):
    '''this function checks if the input is correct and
     returns all the combinations of parentheses in n pairs'''
    str = [""] * 2 * n
    if n > 0 and type(n)==int:
        return parentheses_helper(str, 0,n, 0, 0,[])

def parentheses_helper(str, pointer, n, num_left, num_right,lst):
    '''this function returns all the combinations of parentheses in n pairs'''
    LEFT='('
    RIGHT=')'
    string = ''
    if (num_right == n):
        for i in str:
            string+=i
        lst.append(string)
    else:
        #inserts right parentheses
        if (num_left > num_right):
            str[pointer] = RIGHT
            parentheses_helper(str, pointer + 1, n,num_left, num_right + 1,lst)
        # inserts left parentheses
        if (num_left < n):
            str[pointer] = LEFT
            parentheses_helper(str, pointer + 1, n,num_left + 1, num_right,lst)
    return lst

def up_and_right(n,k):
    '''this function checks if the input is correct and returns all the paths
    from(0,0) to (n,k)'''
    if n==0 and k==0:
        return
    if type(n)==int and type(k)==int and n>=0 and k>=0:
        moves = n + k
        up_and_right_helper(n,k,moves,pointer='')
    else:
        return

def up_and_right_helper(n,k,moves,pointer):
    '''this function returns all the paths possible from (0,0) to (n,k)'''
    MOVE_LST=['r','u']
    if (pointer.count('r') > n or pointer.count('u') > k):
        return
    if  (moves==0):
        print(pointer)
        return
    else:
        for i in MOVE_LST:
            new_pointer = pointer + i
            up_and_right_helper(n,k,moves-1, new_pointer)

def flood_fill(image,start):
    '''this function checks if the input is correct recieves a position on a matrix
    and fills all the empty places that are within reach of the position'''
    if start==() or type(start)!=tuple:
        return
    pointer1=start[0]
    pointer2 = start[1]
    flood_fill_helper(image,pointer1,pointer2)

def flood_fill_helper(image,pointer1,pointer2):
    '''this function recieves a position on a matrix and fills all the empty places
        that are within reach of the position'''
    FILL='*'
    EMPTY='.'
    image[pointer1][pointer2] = FILL
    #checks if all the index around the pointer are fiLled
    if (image[pointer1+1][pointer2]==FILL and image[pointer1][pointer2+1]==FILL
            and image[pointer1-1][pointer2]==FILL and image[pointer1][pointer2-1]==FILL):
        return
    else:
        if image[pointer1+1][pointer2]==EMPTY:
            flood_fill_helper(image, pointer1+1, pointer2)
        if image[pointer1-1][pointer2]==EMPTY:
            flood_fill_helper(image, pointer1-1, pointer2)
        if image[pointer1][pointer2+1]==EMPTY:
            flood_fill_helper(image, pointer1, pointer2+1)
        if image[pointer1][pointer2-1]==EMPTY:
            flood_fill_helper(image, pointer1, pointer2-1)
