import numpy as np
import time as time
import functools

# These are just the Catalan numbers
#
@functools.lru_cache(maxsize=None)
def solution(n, m):
    # m is the number of rows
    if m == 1:
        return n+1
    if m == 0:
        return 1


    if m > 1:
        return sum([solution(i, m-1) for i in range(n+1)])

tic = time.time()
#print(count_paths((2,2)))
print(solution(20,20))

print(time.time()-tic)
