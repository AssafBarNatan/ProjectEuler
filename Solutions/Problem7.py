import numpy as np

# implements is_prime
def isPrime(num: int) -> bool:
    test = 2
    while test <= np.sqrt(num):
        if num % test:
            test +=1
        else:
            return(False)
    return(True)

def Problem7(num:int) -> int:
    i = 1
    index = 1
    while index <= num:
        i += 1
        if isPrime(i):
            index += 1
    return(i)

#def Problem7(num: int) -> int:

#for i in range(10):
#    print(Problem7(i))
print(Problem7(10001))
