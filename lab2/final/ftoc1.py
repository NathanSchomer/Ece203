fahrenheit = 0.0

#converts fahrenheit to celsius
def toCelsius(tmp):
    return (5.0/9.0)*(tmp - 32) 

print "Fahrenheit\tCelsius"

#loop 10 times (increment by 10 each time) until fahrenheit == 100
while fahrenheit <= 100:
    celsius = toCelsius(fahrenheit)
    print "%.0f\t\t%.2f" %(fahrenheit, celsius)
    fahrenheit = fahrenheit + 10.0
