#fahrenheit     celsius     approx      error
#0
#10
#20
#...
#100

fahrenheit = 0.0

def toCelsius(tmp):
    return (5.0/9.0)*(tmp - 32) 

def approxCelsius(tmp):
    return 0.5*(tmp-30)

print "Fahrenheit\tCelsius\t\tEstimation\tError"

while fahrenheit <= 100:
    celsius = toCelsius(fahrenheit)
    approx = approxCelsius(fahrenheit)
    error = celsius - approx
    print "%4.2f\t\t%4.2f\t\t%4.2f\t\t%4.2f" %(fahrenheit, celsius, approx, error)
    fahrenheit = fahrenheit + 100
