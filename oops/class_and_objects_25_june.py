# class and objects

# define python class
class ClassName:
    pass


# Example
class bike:
    name = "hero"
    gear = 0


# python objects
# object_name = class_name()
bike1 = bike()

# modify the name property
bike1.name = "Mountain Bike"

# access the gear property
bike1.gear


# Python Class and Objects
class Bike:
    name = ""
    gear = 0


bike1 = Bike()
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")


# Python Methods
"""We can also define a function inside a Python class. A Python function
defined inside a class is called a method."""


class Room:
    length = 0.0
    breadth = 0.0

    def calculate_area(self):
        area = self.length * self.breadth
        print(area)


study_room = Room()
study_room.length = 5
study_room.breadth = 7
study_room.calculate_area()


# Python Constructors
# Earlier we assigned a default value to a class attribute,
class Bike:
    name = ""


bike1 = Bike()


# However, we can also initialize values using the constructors. For example,


class Bike:
    def __init__(self, name=""):
        self.name = name
        print(self.name)


bike1 = Bike("hero")
