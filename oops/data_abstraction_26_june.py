from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_details(self):
        pass

    def accelerate(self):
        print("speed up...")

    def applied_break(self):
        print("car stop")


class Hatchback(Car):
    def printDetails(self): 
        print("Brand:", self.brand); 
        print("Model:", self.model); 
        print("Year:", self.year); 
    
    def Sunroof(self): 
        print("Not having this feature") 


class Suv(Car): 
    def printDetails(self): 
        print("Brand:", self.brand); 
        print("Model:", self.model); 
        print("Year:", self.year); 
    
    def Sunroof(self): 
        print("Available") 


car1 = Car("alto", 800, 2022)
car2 = Hatchback("maruti", "alto", 2022)
car3 = Suv("suv", 800, 2023)

car1.print_details()
car2.printDetails()
car3.printDetails()


# example 
class Shape(ABC):
    # def __init__(self, length, breath):
    #     self.length = length
    #     self.breath = breath

    length = 5
    breath = 6

    @abstractmethod
    def print_area(self):
        pass

class Rectangle(Shape):
    def print_area(self):
        return self.length * self.breath

class Circle(Shape):
    def print_area(self, radius):
        return 3.14 * radius ** 2


ract = Rectangle()
cr = Circle()
print(ract.print_area())
print(cr.print_area(5))
