import numpy as np

class number:
    def __init__(self,val):
        self.val = val
        primfac = [1]
        d = 2
        while d < self.val + 1:
            if self.val % d == 0:
                primfac.append(d)
            d += 1
        self.factors = primfac

#test = number(39209940)
#print(len(test.factors))

n = 1

while True:
    num1 = number(2*n+1)
    num2 = number((2*n+2)/2)
    if len(num1.factors)*len(num2.factors) > 500:
        print((2*n+1)*(2*n+2)/2)
        break
    n += 1

