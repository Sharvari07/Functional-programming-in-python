def add1(n):
    return n+1

def double(n):
    def add_helper(m,i,j):
        if i == j:
            return m
        else:
            return add_helper(add1(m), add1(i), j)

    return add_helper(n,0,n)

def mul (p,q):                                                                                                               

    def mul_helper(p,q,i,j):

        if p>q and j!=(q-1):
            if i == q+1:
                j = add1(j)
                i = 0 
                p = p - 1
            return mul_helper(add1(p),q,add1(i),j)
        else:
            if q>p and j!=(p-1):
                if i == p+1:
                    j = add1(j)
                    i = 0
                    q = q - 1
                return mul_helper(p,add1(q),add1(i),j)
            else:
                return (q)

    return mul_helper(p,q,0,1)

print(mul(3,4))




#print(double(6))