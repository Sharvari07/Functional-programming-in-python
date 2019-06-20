import time

l_fact  = lambda t: 1 if t==0 else t * l_fact(t-1)

l_timestamp = lambda func, arg: (time.time(), func(arg), time.time())
l_diff = lambda t0,retval, t1: t1 - t0
l_timer = lambda func, arg: l_diff(*l_timestamp(func,arg))

print ("Took: %.5f s" % l_timer(l_fact, 900))