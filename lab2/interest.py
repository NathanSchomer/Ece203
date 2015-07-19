#write a python program that computs how much $1000 will have matured to after 5 years with an interest rate of 0.95% APR

interestRate = 0.95   #percent
time = 5              #years
initial = 1000        #dollars

final = initial * pow( 1 + (interestRate/100), time)

print "After %d years at an interest of %f percent, $%d matured to $%d." %(time, interestRate,initial,final)
