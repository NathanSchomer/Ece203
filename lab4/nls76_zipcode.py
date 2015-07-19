def printDigit(digit):
    bar_weights = [7,4,2,1] #weights for each bar
    bars = [0,0,0,0,0] #five bars per digit
    
    bar_num = 0

    for weight in bar_weights:
        bars[bar_num] = digit // weight
        digit = digit % weight
        bar_num = bar_num + 1
    
    if sum(bars) == 0:
        print [1,1,0,0,0]   #extraneous case when digit = 0
    
    else:
        bars[4] = 2 - sum(bars)
        print bars

def printBarCode(zip_code):
    #print all digit of zip_code
    sumOfDigits = 0
    for i in range(4,-1,-1):
        curr_digit = zip_code // pow(10,i)
        sumOfDigits = sumOfDigits + curr_digit
        printDigit(curr_digit)
        zip_code = zip_code % pow(10,i)
    
    #print sum
    checksum = ((sumOfDigits//10 + 1)*10 - sumOfDigits) % 10
    printDigit(checksum)

printBarCode(95014)
