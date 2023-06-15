import numpy as np

def Problem1(bound: int) -> int:
    #If we list all the natural numbers 
    #below 10 that are multiples of 
    #3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    #
    #Find the sum of all the multiples of 3 or 5 below 1000.

    return(np.floor(bound/3)*(np.floor(bound/3)+1)*3/2 + 
    np.floor(bound/5)*(np.floor(bound/5)+1)*5/2 -
    np.floor(bound/15)*(np.floor(bound/15)+1)*15/2)

print(Problem1(999))
