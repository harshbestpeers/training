# inheritance
"""Python supports class inheritance. It allows us to create a new class
from an existing one."""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("i can eat")


class Dog(Animal):
    def display(self):
        print("my name is ", self.name)


labrador = Dog("rohu")
labrador.eat()
labrador.display()


# Method Overriding in Python Inheritance

"""In the previous example, we see the object of the subclass can access the
method of the superclass.
However, what if the same method is present in both the superclass and subclass
In this case, the method in the subclass overrides the method in the
superclass. This concept is known as method overriding in Python."""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("i can eat")


class Dog(Animal):
    def eat(self):
        print("I like to eat born")


labrador = Dog("rohu")
labrador.eat()


# The super() Function in Inheritance

"""Previously we saw that the same method (function) in the subclass overrides
the method in the superclass.

However, if we need to access the superclass method from the subclass, we use
the super() function. For example,"""


class Fruits:
    def __init__(self, name):
        self.name = name

    def color(self):
        print("fruits are different different colors")


class Apple(Fruits):
    def color(self):
        print("apple color is", self.name)
        super().color()


green_apple = Apple("green apple")
green_apple.color()


# Types of inheritance Python

# 1) Single Inheritance


class Parent:
    def func1(self):
        print("this is a perent class")


class Child(Parent):
    def func2(self):
        print("this is a child class")


obj = Child()
obj.func1()
obj.func2()


# 2) Multiple Inheritance


class Father:

    father_name = ""

    def father(self):
        print(self.father_name)


class Mother:

    mother_name = ""

    def mother(self):
        print(self.mother)


class Son(Father, Mother):
    def perents(self):
        print("father name:", self.father_name)
        print("mother name:", self.mother_name)


s1 = Son()
s1.father_name = "Ram"
s1.mother_name = "Sita"
s1.perents()


# 3) Multilevel Inheritance


class GrandFather:
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name


class Father(GrandFather):
    def __init__(self, father_name, grandfather_name):
        self.father_name = father_name

        GrandFather.__init__(self, grandfather_name)


class Son(Father):
    def __init__(self, son_name, grandfather_name, father_name):
        self.son_name = son_name

        Father.__init__(self, father_name, grandfather_name)

    def print_name(self):
        print("grandfather name :", self.grandfather_name)
        print("father name : ", self.father_name)
        print("son name : ", self.son_name)


s1 = Son("Prince", "Rampal", "Lal mani")
print(s1.grandfather_name)
s1.print_name()


# 4) Hierarchical Inheritance


class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# 5) Hybrid inheritance


class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


object = Student3()
object.func1()
object.func2()
