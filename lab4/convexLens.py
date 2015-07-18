import math
import random

def scramble(word):
    if len(word) > 3:
        result = word[0]
        substr = word[1:(len(word)-1)]
            
        tmp = random.sample(substr,len(substr))
        for  thisChar in tmp:
            result = result + thisChar
        return result + word[len(word)-1]
    else:
        return word

def scramble_sentence(sen):
    result = ""
    for word in sen.split(" "):
        result = result + scramble(word) + " "
    return result

def f(r1, r2, d, n):
    return pow((n-1.0)*((1.0/r1)-(1.0/r2)+(((n-1.0)*d)/(n*r1*r2))), -1.0)


#print "%f" %f(.12,.18,0.2,1.8)
print "%s" %scramble_sentence("I hope this function works properly")

