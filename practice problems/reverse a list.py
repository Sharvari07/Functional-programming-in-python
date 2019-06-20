lis = list(input())

def len_of_list():
    leng = sum(map(lambda x:1 , lis)) 
    return leng

def last_element(lis,i):
    if i <= len_of_list():
        return last_element(lis, i+1)
    else:
        return lis[i]

def reverse_a_list(lis, i):
    a = []
    j = i - 1
    a[i] = last_element(lis,j)
    return reverse_a_list(lis, i+1)
