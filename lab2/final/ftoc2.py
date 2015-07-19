fahrenheit = 0.0

#converts fahrenheit temperature to celsius
def toCelsius(tmp):
    return (5.0/9.0)*(tmp - 32) 

#approximates celsius temperature from fahrenheit
def approxCelsius(tmp):
    return 0.5*(tmp-30)

print "Fahrenheit\tCelsius\t\tEstimation\tError"

#loop 10 times (increment by 10 each time) utnil fahrenheit == 100
while fahrenheit <= 100:
    celsius = toCelsius(fahrenheit)
    approx = approxCelsius(fahrenheit)
    error = celsius - approx            #difference between actual and approximated
    print "%.0f\t\t%.2f\t\t%.2f\t\t%.2f" %(fahrenheit, celsius, approx, error)
    fahrenheit = fahrenheit + 10.0
