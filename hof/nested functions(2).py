
l_fact  = lambda t: 1 if t==0 else t * l_fact(t-1)

def mul_chain(*xyz):
    total = 1
    for (func, arg) in xyz:
        total *= func(arg)
    return total

t = mul_chain((l_fact,3),(l_fact,5))
print (t)