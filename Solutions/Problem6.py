import numpy as np

def squareDiff(num: int) -> bool:
    out = 0

    for n in range(num+1):
        out += n*(n**2-n)

    return(out)

print(squareDiff(100))
