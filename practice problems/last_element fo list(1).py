import random

ls = [random.randint(0,20) for i in range(10)]

print(ls)

def find_last(list, index):
    if index == len(list) - 1:
        return list[index]
    else:
        return find_last(list, index + 1)

print("The last number of the list is:",find_last(ls, 0))

