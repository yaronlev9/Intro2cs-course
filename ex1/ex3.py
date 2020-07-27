def input_list():
    """this function asks the user for a string and returns a list
    of the strings given"""
    new_list = []
    while True:
     string_from_user=input()
     if string_from_user=='':
        return new_list
     print(string_from_user)
     new_list.append(string_from_user)

def concat_list(str_list):
    """this function takes a list and returns a string with a concetation
     of the parameters in the list"""
    if str_list ==[] or str_list==['']:
        return '""'
    string=''+str_list[0]
    for i in range(len(str_list)-1):
        string+=" "+str_list[i+1]
    return string+''

def maximum(num_list):
    """this function takes a list of numbers and returns the maximum"""
    if num_list==[]:
        return None
    max = num_list[0]
    for i in range(len(num_list)-1):
        if max<=num_list[i+1]:
            max=num_list[i+1]
    return max

def cyclic(lst1, lst2):
    """this function recieves two lists and returns true if the first one
     is a cyclic permutatin of the second"""
    if len(lst1)!=len(lst2):
        return False
    if lst1==[] and lst2==[]:
        return True
    count=0
    for m in range(len(lst1)):
        lst1.insert(0, lst1[len(lst1)-1])
        lst1=lst1[0:len(lst1)-1]
        if  lst1==lst2:
            count+=1
    if count==1:
        return True
    else:
        return  False

def seven_boom(n):
    """this function recieves an integer and returns a list of strings
    that replaces every number divided by 7 or has 7 to 'boom'"""
    list1=list(range(1,n+1))#creating a list from 1 to n
    string1 =str(list1[0])
    for i in range(len(list1)):
        if list1[i]%7==0:
            list1 = list1[0:i]+list1[i+1:]
            list1.insert(i, "boom")
        elif '7' in str(list1[i]) :
            list1 = list1[0:i] + list1[i + 1:]
            list1.insert(i, "boom")
    for j in range(len(list1) - 1): #this loop converts the list to strings as asked
        string1 += ' ' + str(list1[j + 1])
    return [string1]

def histogram(n, num_list):
    """this function recieves an integer and a list of numbers and returns the histogram"""
    list_histogram=[]
    for j in range(0,n):
        count = 0
        for i in range(len(num_list)):
            if j==num_list[i]:
                count+=1
        list_histogram.append(count)
    return list_histogram

def prime_factors(n):
    """this function recieves an integer and returns a list of the prime numbers
     that it contains"""
    if n==1:
        return []
    prime_list = []
    for i in range(2,n+1):
        while n%i==0:
            prime_list.append(i)
            n=n/i
    return prime_list

def cartesian(lst1, lst2):
    """this function recieves 2 lists and returns the cartesian multiplication"""
    if lst1==[] or lst2==[]:
        return []
    list_cartesian=[]
    for j in range(len(lst1)):
        for i in range(len(lst2)):
            list_cartesian.append([lst1[j],lst2[i]])
    return list_cartesian

def pairs(num_list, n):
    """this function recieves a list of integers and a number and returns all the pairs
    which their sum equals the number"""
    list_pairs=[]
    if num_list==[]:
        return []
    for i in range(len(num_list)):

        for j in range(len(num_list)):
            if num_list[i]+num_list[j]==n and num_list[i]!=num_list[j]:
                list_pairs.append([num_list[i], num_list[j]])
                if [num_list[i],num_list[j]] in list_pairs and [num_list[j],num_list[i]] in list_pairs:
                    list_pairs.remove([num_list[j],num_list[i]])
    return list_pairs

