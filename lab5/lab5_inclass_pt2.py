import math

def diameter(wire_guage):
    return 0.127*pow(92.0, (36.0-wire_guage)/39.0)

def resistance(P,L,wire_guage):
    return (4.0*P*L)/(math.pi*pow(diameter(wire_guage),2))
    
def copper_wire_resistance(length, wire_guage):
    resistivity = 1.678*pow(10, -8)
    return resistance(resistivity, length, wire_guage)

def aluminum_wire_resistance(length, wire_guage):
    resistivity = 2.82*pow(10, -8)
    return resistance(resistivity, length, wire_guage)

print "1 m, 35 AWG copper: \t%0.8e ohms" %copper_wire_resistance(1, 35)
print "20 m, 17 AWG aluminum: \t%0.8e ohms" %aluminum_wire_resistance(20, 17)
