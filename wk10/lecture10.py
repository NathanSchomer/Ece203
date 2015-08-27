class Person:
    """
    This is the docstring for the Person class !!
        
        The Person class (losoely) represents a person
   
        attributes:
            -age
            -weight

        methods:
            -gain_weight()
            -lose_weight()
            -have_birthday()
    """

    def __init__(self, age, weight):
        self.age = age  #initialize attribute of object
        self.weight = weight

    def gain_weight(self, amount):
        """Add 'amount' weight to a PErson object"""
        self.weight += amount

    def lose_weight(self, amount):
        """Remove 'amount' weight to a Person object"""
        self.weight -= amount

    def have_birthday(self):
        """Increase the age of a Person object by 1"""
        self.age += 1

if __name__ == "__main__":

    #joe = Person(12,88) #instance (or object) of class
    #bob = Person(30, 155)

    people = {}

    people['joe'] = Person(12, 88)
    people['bob'] = Person(30, 155)

    people['bob'].have_birthday()
    
    print "Joe's age: {}".format(people['joe'].age)
    print "Bob's weight: {}".format(people['bob'].weight)

    people['joe'].have_birthday()
    people['bob'].lose_weight(5)

    print "\nJoe's new age: {}".format(people['joe'].age)
    print "Bob's new age: {}".format(people['bob'].age)

