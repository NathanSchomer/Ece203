a = 3
b = 5

a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = pow((a+b),2)
eq2_pow = pow((a-b),2)

print '1st equation: %g = %g' % (eq1_sum, eq1_pow)
print '2nd equation: %g = %g' % (eq2_sum, eq2_pow)
