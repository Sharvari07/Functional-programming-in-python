''' l = input()


#j = sum(map(lambda x: 1, user_input()))

def no_of_elements(l,i):
    if isinstance(l,list):
        return True
        print("Yes")
    else:
        return False
 

k = no_of_elements(l, 0)
print("No of elements are:", k) '''

import random
ls = [random.randint(0,20) for i in range(10)]

print(ls)

''' def len_of_list(ls,i):
    if ls[i] != None:
        print (ls[i])
        return len_of_list(ls, i+1)
    else:
        return i
 '''
leng = sum(map(lambda x:1 , ls)) 


#j = len_of_list(ls,0)
print(leng)
