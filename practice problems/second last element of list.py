import random

ls = [random.randint(0,20) for i in range(10)]

print(ls)

def find_second_last(list, index):
    if index == len(list) - 2:
        return list[index]
    else:
        return find_second_last(list, index + 1)

print("The second last number of the list is:",find_second_last(ls, 0))