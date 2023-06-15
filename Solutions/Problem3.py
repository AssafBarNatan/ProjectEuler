import numpy as np

def isPrime(num: int) -> bool:
    test = 2
    while test <= np.sqrt(num):
        if num % test:
            test +=1
        else:
            return(False)
    return(True)

def Problem3(num: int) -> int:
    # Finds largest prime factor in the dumb way
    
    pf = 2
    cand = 2
    tmp_num = num

    while cand < np.sqrt(tmp_num):
        if isPrime(tmp_num):
            return(tmp_num)
        if tmp_num % cand == 0:
            tmp_num = tmp_num/cand
            pf = max(cand,pf)
            cand = 2
        else:
            cand +=1
    return(pf)

print(Problem3(600851475143))
#print(Problem3(15))
