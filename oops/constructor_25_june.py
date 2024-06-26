"""The task of constructors is to initialize(assign values) to the data
members of the class when an object of the class is created."""

# default constructor
class GirlsCollage:
    def __init__(self):  # default constructor
        self.gender = "girl"

    def details(self, name, age):
        self.name = name
        self.age = age
        return self.name, self.age, self.gender


obj = GirlsCollage()
p1 = obj.details("ranu", 12)

print(p1)


# parameterized constructor
class Collage:
    def __init__(self, name, age, gender):  # parameterized constructor
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print("name: ", self.name)
        print("age: ", self.age)
        print("gender: ", self.gender)


obj1 = Collage("qwer", 22, "male")
obj1.details()


# we define a class MyClass with both a default constructor and a parameterized constructor
class MyClass:
    def __init__(self, name=None):
        if name is None:
            print("default constructor is called")
        else:
            print("parameterized constructor is called")


obj1 = MyClass("harsh")
obj2 = MyClass()


# Destructors in Python
"""Destructors are called when an object gets destroyed. In Python, destructors are 
not needed as much as in C++ because Python has a garbage collector that handles memory 
management automatically. """


class Employee:
    def __init__(self):
        print("Employee is created")

    def __del__(self):
        print("destructor called, employee deleted")


obj = Employee()

""" NOTE: The destructor was called after the program ended or when all the 
references to object are deleted""" 
