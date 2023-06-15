import numpy as np
import time as time

# Want to find the sum of the digits of 2^(1000)

def sieveEratosthenes(n):
    primeQ = [True]*n
    primeQ[0] = primeQ[1] = False
    for (i, isprime) in enumerate(primeQ):
        if isprime:
            yield i
            for k in range(i*i, n, i):
                primeQ[k] = False

def ridDigit(p, dig):
    return(str(p).replace(str(dig),"-"))

primes = []

mydic = {}

tic = time.time()
## This solution works for small numbers, but didn't work for 
# larger ones
#for p in sieveEratosthenes(10**9): #(10**8):
#    for dig in set([digit for digit in str(p)]):
#        if ridDigit(p, dig) in mydic:
#            mydic[ridDigit(p, dig)].append(p)
#            if len(mydic[ridDigit(p, dig)]) > 7:
#                print(mydic[ridDigit(p,dig)])
#        else:
#            mydic[ridDigit(p, dig)] = [p]
#
#print(mydic)

print(time.time()-tic)
