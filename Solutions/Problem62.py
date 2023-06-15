import numpy as np
import time as time

d = {}
i = 0

t = time.time()
while True:
    l = tuple(sorted([dig for dig in str(i**3)]))
    #print(l)
    if l in d.keys():
        d[l].append(i**3)
    else:
        d[l] = [i**3]

    if len(d[l])>4:
        print(min(d[l]))
        print(i)
        break
    i += 1

print(time.time()-t)
