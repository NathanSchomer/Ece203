#class sodaCan
    #getSurfaceArea()
    #getVolume()
    # *height and radius speicifed upon instantiation

import math

class SodaCan:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def getSurfaceArea(self):
        #height * circumfrence + 2*area pf bottom
        return self.height*(2*math.pi*self.radius) + 2*math.pi*self.radius**2

    def getVolume(self):
        #height * area of bottom
        return self.height*(math.pi*self.radius**2)


class Car:
    def __init__(self, mpg):
        self.mpg = mpg  #miles / gallon
        self.tank = 0   #gallons
    
    def drive(self,dist):
        self.tank -= dist/self.mpg

    def get_gas_level(self):
        return self.tank

    def add_gas(self, gas):
        self.tank += gas

class Bug:
    def __init__(self,pos):
        self.direction = 1
        self.pos = pos

    def turn(self):
        self.direction *= -1

    def move(self):
        self.pos += self.direction

    def getPosition(self):
        return self.pos


if __name__ == "__main__":
    pepsi = SodaCan(5,2)
    print "\nSodaCan object created with height = 5 and radius = 2..."
    print "Soda Area:\t%0.4f" % pepsi.getSurfaceArea()
    print "Soda Volume:\t%0.4f\n" % pepsi.getVolume()
    
    jetta = Car(50)
    jetta.add_gas(20)
    jetta.drive(100)
    print "Car's fuel level: %d\n" % jetta.get_gas_level()

    ladybug = Bug(10)
    ladybug.move()
    ladybug.move()
    ladybug.move()
    ladybug.turn()
    ladybug.move()
    print "Actual bug position %d\nExpected position: 12\n" % ladybug.getPosition()

