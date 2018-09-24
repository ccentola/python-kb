# Animal is-a object
# using "object" is not required, but in python it is better to be explicit than impliciet
class Animal(object):
    pass
    
# dog is-a animal
class Dog(Animal):
    
    def __init__(self,name):
        
        # dog has-a name
        self.name = name
        
# cat is-a animal
class Cat(Animal):
    
    def __init__(self,name):
        
        # cat has-a name
        self.name = name

# Person is-a object        
class Person(object):
    
    def __init__(self, name):
        
        # person has-a name
        self.name = name
        
        # person has-a pet
        self.pet = None
        
# Employee is-a person
class Employee(Person):
    
    def __init__(self,name,salary):
        
        # employee has-a name (inhereted from Person)
        super(Employee,self).__init__(name)
        
        # employee has-a salary
        self.salary = salary

# fish is-a object        
class Fish(object):
    pass
    
# salmon is-a fish
class Salmon(Fish):
    pass
    
# halibut is-a fish
class Halibut(Fish):
    pass
    
# rover is-a dog
rover = Dog("Rover")

# satan is-a cat
satan = Cat("Satan")

# mary is-a person
mary = Person("Mary")

# mary has-a pet or
# mary has-a pet that is-a cat that has-a name satan
mary.pet = satan

# frank is-a person who is-a employee who has-a 120000 salary
frank = Employee("Frank", 120000)

# frank has-a pet who is-a dog who has-a name rover
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = Salmon()

# harry is-a halibut
harry = Halibut()