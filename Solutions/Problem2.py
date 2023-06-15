import numpy as np

def Problem1(bound: int) -> int:
    #Each new term in the Fibonacci sequence is generated 
    #by adding the previous two terms. By starting with
    #1 and 2, the first 10 terms will be:
    #
    #1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    #
    #By considering the terms in the Fibonacci sequence 
    #whose values do not exceed four million, 
    #find the sum of the even-valued terms.
    
    phi = (1 + np.sqrt(5))/2
    psi = 1-phi

    # fib_ind is the largest fibbonacci index which is divisible by 3, and 
    # for which f_(fib_ind) is smaler than bound. This algorithm sucks 
    # ass, but it worked.

    a  = 0
    b = 1
    fib_ind = 1
    while b < 4000000:
        print(a)
        tmp = b
        b = a+b
        a = tmp
        fib_ind += 1
    print(fib_ind)

    return(1/(np.sqrt(20))*((1-phi**fib_ind)/(1-phi) - (1-psi**fib_ind)/(1-psi)))

print(Problem1(4000000))
