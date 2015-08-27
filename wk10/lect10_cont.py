from lecture10 import Person

class People:
    """
    This is the docstring for the People class

        The people class wraps the person class to allow a user to 
        create multiple peron objects.
    """

    def __init__(self):
        self.people = {}

    def add(self):
        print "__________________"
        name = raw_input(" Name: ")
        if name == '':
            return False

        age = raw_input("   Age: ")
        weight = raw_input(" Weight: ")

        self.people[name] = Person(age, weight)
        return True

    def show(self):
        for name, person in self.people.items():
            print name
            print '    age: {}'.format(person.age)
            print ' weight: {}'.format(person.weight)

if __name__=="__main__":

    #good data structures = easy to read code!
    people = People()

    while people.add():
        pass

    people.show()
