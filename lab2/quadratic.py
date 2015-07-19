from math import sqrt

a = 7
b = 26
c = 3

q = sqrt(b*b - 4*a*c)

x1 = (-b + q) / (2*a)
x2 = (-b - q) / (2*a)

print """
x1 = %g
x2 = %g
""" % (x1, x2)
