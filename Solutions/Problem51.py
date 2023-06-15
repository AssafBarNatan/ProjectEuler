import numpy as np
import time as time

#want to find a prime p = abcdefg... such that replacing indices 
#with a constant number gives 8 different primes

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

#def replaceDigits(p):
#    out = [p]
#    for dig in range(9):
#        out.append(int(str(p).replace(


mydic = {}

tic = time.time()

primes = [p for p in sieveEratosthenes(10**6)]
## This solution works for small numbers, but didn't work for 
# larger ones
for p in primes: #(10**8):
    for dig in set([digit for digit in str(p)]):
        blank = ridDigit(p, dig)
        if blank in mydic:
            for d in range(10):
                if int(blank.replace("-", str(d))) in mydic:
                    mydic[blank].append(int(blank.replace("-",str(d))))
            if len(mydic[blank]) > 7:
                print(mydic[blank])
        else:
            mydic[blank] = [p]

print(mydic["-2-3-3"])


print(time.time()-tic)
