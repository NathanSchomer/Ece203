limit = 0

# continue to prompt user for input until valid value is etnered
while limit == 0:
    try:
        limit = int(raw_input('\nlimit: '))
    except:
        print '\nInvalid input.'

total = 0.0 #total of summation

#calculate summation by looping "limit" number of times
for i in range(1,limit + 1):
    total = total + (1 / float(i)) #add 1/[count] to total

print "Summation Total: %.3f" %(total)
