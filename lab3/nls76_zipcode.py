def printDigit(digit):
    bars = [0,0,0,0,0] #five bars per digit

    bars[0] = digit / 7 
    bars[1] = digit / 4
    bars[2] = digit / 2
    bars[3] = digit / 1

    if(bars[]
    
    
    print "digit"

def printBarCode(zip_code):
    bars = [0,0,0,0,0] #five bars per digit
    
    bars[0] = zip_code / 7
    zip_code = zip_code % 7

    bar2 = zip_code / 4 
    zip_code = zip_code % 4
    
    bar3 = zip_code / 2
    
    bar4 = zip_code

    if(bar1 + bar2 + bar3 + bar4 < 2)
        bar5 = 0;
    
    print "zip_code"

printBarCode(15601)
