import random

'''ls = [random.randint(0,20) for i in range(10)]

print(ls)
'''

def user_input():
    i = input("Enter any list or string:")
    if isinstance(i, (list,str)):
        print ("Valid input")
        return i
    else:
        print ("Please enter a valid input",user_input())

def kth_input():
    k = int(input("Enter the kth index:"))
    return k

def find_kth_element(l, index, no):
    if index == no:
        return l[index]
    else:
        return find_kth_element(l, index + 1, no)


j = find_kth_element(user_input(), 0, kth_input())
print ("The kth element is:", j)
    