
from ex3 import maximum
def test():
    """this function tests the function maximum"""
    test1=maximum([1, 1, 2, 2])
    test2=maximum([0, 0, 0, 0])
    test3=maximum([1, 2, 3, 4])
    test4=maximum([5, 4, 3, 2])
    tests=list([test1,test2,test3,test4])
    answers=list([2,0,4,5])
    count=0
    for i in range(4):
        if tests[i]==answers[i]:
            print("test",i+1,"OK")
            count+= 1
        else:
            print("test", i + 1, "FAIL")
            count -= 1
    if count==4:
        return True
    else:
        return False




if __name__ == '__main__':
    test()
