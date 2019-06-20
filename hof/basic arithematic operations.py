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
    a = p
    b = q                                                                                                            

    def mul_helper(p,q,i,j):

        if p>q and j!=(q):
            if i == a:
                j = add1(j)
                i = 0 
                
            return mul_helper(add1(p),q,add1(i),j)
        elif q>p and j!=(p):
            if i == b:
                j = add1(j)
                i = 0
            return mul_helper(p,add1(q),add1(i),j)
        elif q == p and j!=(p):
            if i == (add1(p)):
                j = add1(j)
                i = 0
            return mul_helper(add1(p),q,add1(i),j)
        else:
            if p>q:
                return (p-1)
            elif q>p:
                return (q-1)
            else:
                return (p-1)

    return mul_helper(p,q,0,1)
'''

    def mul_helper(p,q,j):
        if p>q and j!=(q):

            return mul_helper(double(p),q,add1(j))

        elif q>p and j!=(p):

            return mul_helper(p,double(q),add1(j))
        
        elif q==p and j!=(p):

            return mul_helper(p,double(q),add1(j))

        else:
            if p>q:
                return (p-1)
            elif q>p:
                return (q-1)
            else:
                return (p-1)

    return mul_helper(p,q,1)
            
'''

print(mul(4,5))




#print(double(6))