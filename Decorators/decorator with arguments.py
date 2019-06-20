import time

def timer_argument(units = 's'):

    def timer(func):

        def inner(*args, **kwargs):

            t0 = time.time()
            func(*args, **kwargs)
            t1 = time.time()
            diff = t1-t0
            if units == 'ms':
                diff *= 100
            return diff
        return inner

    return timer

@timer_argument(units = 'ms')
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

f = factorial(100)
print (f)