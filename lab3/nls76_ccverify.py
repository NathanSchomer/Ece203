#get input from user
card  = raw_input("credit card number: ")

totalSum = 0

#iterate through each number of the card starting with the rightmost digit
for pos in range(len(card)-1, -1, -1):
    #starting with the last digit, add every other digit to the sum
    if (pos) % 2 == 1:
        totalSum = totalSum + int(card[pos])
    #for the other digits, multiply them by two and add the digits of the product to the sum
    else: 
        totalSum = totalSum + (2*int(card[pos]) % 10) + (2*int(card[pos]) // 10) #sum digits
   
#if the digit in the 1's place of the sum is 0, the card number is valid
if totalSum%10 == 0:
    print "%s is a VALID credit card number." %card
else:
    print "%s is an INVALID credit card numer." %card
