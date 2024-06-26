# Polymorphism in Python

"""The literal meaning of polymorphism is the condition of occurrence in
different forms.
Polymorphism is a very important concept in programming. It refers to the use
of a single type entity (method, operator or object) to represent different
types in different scenarios."""

# Example
"""We know that the + operator is used extensively in Python programs.
But, it does not have a single usage."""

# for integer data type
num1 = 1
num2 = 2
num3 = num1 + num2  # + operator is used to perform addition operation.
print(num3)

# for string data type
name = "harsh"
sname = "patidar"
full_name = name + sname  # + operator is used to perform concatenation.
print(full_name)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow Meow Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark Bark Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()



# example
class Car:
    def __init__(self, brand, model):
        self.model = model
        self.name = name

    def move(self):
        print("Drive")


class Boat:
    def __init__(self, brand, model):
        self.model = model
        self.name = name

    def move(self):
        print("Sail")


class Plane:
    def __init__(self, brand, model):
        self.model = model
        self.name = name

    def move(self):
        print("Fly")


car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747") 

for x in (car1, boat1, plane1):
    x.move()
