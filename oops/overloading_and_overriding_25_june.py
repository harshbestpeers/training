# overriding in python
class Parents:
    def my_method(self):
        print("calling parents class")


class Child(Parents):
    def my_method(self):
        print("calling child class")

c1 = Parents()
c1.my_method()
c2 = Child()
c2.my_method()

# Example
class Employee:
    def __init__(self, emp_name, emp_salary):
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def get_name(self):
        return self.emp_name

    def get_salary(self):
        return self.emp_salary

class SalesOfficer(Employee):
    def __init__(self, emp_name, emp_salary, increment):
        super().__init__(emp_name, emp_salary)  
        self.increment = increment

    def get_salary(self):
        return self.emp_salary + self.increment

    
emp = Employee("harsh", 50000)
print(f"employee name {emp.get_name()} and employee salary {emp.get_salary()}")

sales = SalesOfficer("anklit", 50000, 10000)
print(f"employee name {sales.get_name()} and employee salary {sales.get_salary()}")


# overloading in python

class Employee:
    def details(self, name, age):
        self.name = name
        self.age = age
        return self.name, self.age

    def detail(self, name, age, gender): 
        self.name = name
        self.age = age
        self.gender = gender
        return self.name, self.age, self.gender


emp = Employee()
a = emp.detail("harsh", 22)  # overloading not allow in python