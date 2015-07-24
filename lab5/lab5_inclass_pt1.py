#accept integer X
#return list of integers

def int2binarylist(X):
    binStr = bin(X)
    binStr = binStr[2:len(binStr)] #remove binary prefix

    binList = []
    count = 0;

    for ch in binStr:
        binList.append(int(ch)) 
    
    print binList
