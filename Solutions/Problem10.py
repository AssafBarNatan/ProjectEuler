import numpy as np

def isPrime(num: int) -> bool:
    test = 2
    while test <= np.sqrt(num):
        if num % test:
            test +=1
        else:
            return(False)
    return(True)


def sumPrimes(num: int) -> bool:
    tot = 0
    i = 2
    while i < num:
        tot += (i if isPrime(i) else 0)
        i+= 1
        if i%100000 ==0:
            print(i)
    return(tot)



print(sumPrimes(2000000))

