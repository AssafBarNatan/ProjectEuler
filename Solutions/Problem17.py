import numpy as np
import time as time

# Want to find the number of letters when we write out all 
# the numbers from 1 to 1000 in words

def word(n, decoration = 0):
    numnames = ["one", "two", "three", "four", "five", "six", "seven", 
            "eight", "nine", "ten"]
    if decoration == 0:
        return(numnames[n-1])
    if decoration == 1:
        if n==2:
            return("twen")
        if n==3:
            return("thir")
        if n==4:
            return("for")
        if n==5:
            return("fif")
        if n==8:
            return("eigh")
        return(numnames[n-1])

def namesOfPowers(power):
    powers = ["hundred", "thousand", "million", "billion", "trillion"]
    return(powers[power-2])

def writeInWords(n):
    # This deals with numbers less than 100
    if n == 1000:
        return("onethousand")
    if n < 11:
        return(word(n))
    elif n == 11:
        return("eleven")
    elif n == 12:
        return("twelve")
    elif n == 14:
        return("fourteen")
    elif n < 20:
        return(word(n % 10, 1) + "teen")
    elif n < 100:
        if n % 10 == 0:
            return(word(int(n/10),1) + "ty")
        else: 
            return(word(int(n/10),1) + "ty" + word(n % 10))

    digits = int(np.log10(n))



    #return(writeInWords(int(n/1000) % 10) + "thousand" + writeInWords(n-1000*int(n/1000)))

    if n % 100:
        return(word(int(n/100)) + "hundred" + "and" + writeInWords(n-100*int(n/100)))
    else: 
        return(word(int(n/100)) + "hundred")

totlen = 0
for i in range(1,1001,1):
    totlen += len(writeInWords(i))
    #print(writeInWords(i))

#print(totlen)


print(writeInWords(788))




