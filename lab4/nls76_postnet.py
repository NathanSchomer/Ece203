#function to print one digit of POSTNET barcode
def printDigit(digit):
    bar_weights = [7,4,2,1] #weights for each bar
    bars = [0,0,0,0,0]      #five bars per digit    
    
    bar_num = 0             #counter for bar position within current digit

    #determine if each bar is high(1) or low(0)
    for weight in bar_weights:
        bars[bar_num] = digit // weight
        digit = digit % weight
        bar_num = bar_num + 1
    
    #check for extraneous case when digit = 0
    if sum(bars) == 0:
        bars = [1,1,0,0,0]
    else:
        bars[4] = 2 - sum(bars)
        
    for i in bars:
        if i == 1:
            print "!",  #tall bar
        else:
            print ".",  #short bar

#function to print full barcode
def printBarCode(zip_code):
    sumOfDigits = 0
    for i in range(4,-1,-1):
        curr_digit = zip_code // pow(10,i)
        sumOfDigits = sumOfDigits + curr_digit
        printDigit(curr_digit)
        zip_code = zip_code % pow(10,i)
    
    #calculate and print checksum
    checksum = ((sumOfDigits//10 + 1)*10 - sumOfDigits) % 10
    printDigit(checksum)

printBarCode(95014) 
