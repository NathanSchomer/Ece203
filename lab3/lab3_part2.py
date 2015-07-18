#generate two random numbers
    #y-axis location
    #angle wrt y-axis

from random import random
from math import pi, sin

ytail = 0
theta = 0
yhead = 0

hits = 0
#ttempts = int(raw_input('Attempts: '))

i = 1
j = 0

while i <= 7:
    while j <= pow(10,i):
        ytail = 2*random()
        theta = pi*random()
        yhead = ytail + sin(theta)
        if yhead > 2:
            hits = hits + 1
        j = j + 1
    print "ratio: %f" %(pow(10,i)/hits)
    i = i + 1
