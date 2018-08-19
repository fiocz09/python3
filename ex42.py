# Fish is a class, and Salmon is a class, and Mary is an object.

## Animal is-a object
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee is-a Person who has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet which is satan
mary.pet = satan

## frank is-a Employee, who has-a name Frank and has-a salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet which is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

# Then enter python
# import this file like >> import ex42
# look up frank's salary like >> ex42.frank.salary
# look up mary's pet's name like >> ex42.mary.pet.name
