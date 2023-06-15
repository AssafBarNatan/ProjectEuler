import numpy as np

def isPalindrome(num: int) -> bool:
    dig = [d for d in str(num)]

    for ind, d in enumerate(dig):
        if dig[ind] != dig[len(dig)-ind-1]:
            return(False)

    return(True)
        


def Problem4(num: int) -> int:
    # Finds largest palindrome number which factors as two [num]-digit 
    # numbers (for example, 9009 = 99*91)

    palin_cand = 10**(2*num-2)
    fac1 = 10**(num-1)
    fac2 = fac1
    while fac2 < 10**num:
        tmp = fac1
        fac1 = (10*(num-1) if fac1==fac2 else fac1 + 1)
        fac2 = (fac2+1 if tmp == fac2 else fac2)
        #print("first factor: " + str(fac1) + " second factor: " + str(fac2))

        if isPalindrome(fac1*fac2):
            palin_cand = max(palin_cand,fac1*fac2)
            print(fac1,fac2)
    return(palin_cand)

#print(Problem3(600851475143))
print(Problem4(3))
