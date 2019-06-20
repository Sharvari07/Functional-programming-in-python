import operator


l_fact  = lambda t: 1 if t==0 else t * l_fact(t-1)

def mul_chain(how, *xyz):
    total = 1
    for (func, arg) in xyz:
        total = how(total,func(arg))
    return total

t = mul_chain(operator.mul,(l_fact,3),(l_fact,5))
t1 = mul_chain(operator.add,(l_fact,3),(l_fact,5))
t2 = mul_chain(operator.truediv,(l_fact,3),(l_fact,5))
print (t, t1, t2)