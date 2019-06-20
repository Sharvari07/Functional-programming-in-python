import random

ls = [random.randint(0,20) for i in range(10)]
print (ls)

l = len(ls)

'''
for x in range(l):
    if x == l-1:
        print("last number is:", ls[x])
 '''   
'''
last = [print("Last no is:",ls[x]) for x in range(l) if x==(l-1)]

def find_last(list, index):
    if index == len(list) - 1:
        return list[index]
    else:
        find_last(list, index+1)

find_last(list, 0)

[n in next_prime(100)]
map(find_last, list_of_lsitsfind_last(x)
'''