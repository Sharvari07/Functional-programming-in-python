import math
from functools import reduce
import operator

def clist (*args):
    a = list(*args)
    return a

d = (1,2,3,4,5)
print(clist(d))

def add (*args):
    b = sum(clist(*args))
    return b

def subtraction (*args):
    sub = reduce(operator.sub, clist(*args))
    return sub

def negate (args):
    negate1 = operator.mul(-1,args)
    return negate1

print(add(d))
print(subtraction(d))
print(negate(1))
