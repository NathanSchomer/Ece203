#prompt user for:
    #B -> rate of predation
    #C -> rate at which predator deaths exceed births w/o food
    #D -> predator increase in presence of food

#prompt users for rates, initial population sizes, and time
#print populations for given number of years after sim has finished

#default values:
    #A = 0.1
    #B = 0.01
    #C = 0.01
    #D = 0.00009
    #iniitalPrey = 1000
    #initialPredators = 1000
    #t = 30 #years

default_A = 0.1
default_B = 0.01
default_C = 0.01
default_D = 0.00009
default_t = 30.0 #years
default_predators = 20.0
default_prey = 1000.0

A = float(raw_input() or default_A)
B = float(raw_input() or default_B)
C = float(raw_input() or default_C)
D = float(raw_input() or default_D)
initialPrey = int(raw_input() or default_prey)
initialPredator = int(raw_input() or default_predators)
time = int(raw_input() or default_t)

prey = int(initialPrey)
pred = int(initialPredator)

i = 0
while pred > 0:
    last_prey = prey
    last_pred = pred
    prey = int(last_prey*(1+A-B*last_pred))
    pred = int(last_pred*(1-C+D*last_prey))
    i = i + 1

print 'Prey %d' %(prey)
print 'Predators %d' %(pred)
print 'time %d' %(i)
