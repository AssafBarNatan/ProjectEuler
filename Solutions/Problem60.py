import numpy as np
import itertools
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

def isPrime(n):
    d = 2
    while d*d < n:
        if n % d == 0:
            return(0)
        d += 1
    return(1)

def concatPrimes(p):
    out = []
    for cat in ["3", "7", "109", "673"]:
        out.append(int(str(p) + cat))
        out.append(int(cat + str(p)))
    return(out)

tic = time.time()

primes = [p for p in sieveEratosthenes(10**6)]

## Brute force approach -- this does not work.
#N = 1000
#for ind in range(N):
#    for jnd in range(ind,N):
#        for knd in range(jnd,N):
#            for lnd in range(knd, N):
#                p1 = primes[ind]
#                p2 = primes[jnd]
#                p3 = primes[knd]
#                p4 = primes[lnd]
#                #p5 = primes[mnd]
#                primvec = [p1, p2, p3, p4]
#                tuples = itertools.combinations(primvec, 2)
#                good = 1
#                for pair in tuples:
#                    if int(str(pair[0]) + str(pair[1])) not in primes or int(str(pair[0]) + str(pair[1])) not in primes:
#                        good = 0
#                if good:
#                    mysum = min(mysum, sum(primvec))
#print(mysum)

print(time.time()-tic)
