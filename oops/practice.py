from datetime import date

# Example 1
"""1. Write a  Python program to create a class representing a Circle. Include
methods to calculate its area and perimeter. """


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius ** 2
        print("area of circle is ", area)

    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        print("perimeter of circle is ", perimeter)


c = Circle(12)
c.area()
c.perimeter()

# Example 2
"""2. Write a  Python program to create a person class. Include attributes
like name, country and date of birth. Implement a method to determine the
person's age."""


class person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


p = person("harsh", "india", date(2002, 10, 29))
print(p.age())

# Example 3
"""3. Write a Python program to create a calculator class. Include methods for
basic arithmetic operations."""


class Calculate:
    def add(self, x, y):
        self.x = x
        self.y = y
        print("x + y = ", x + y)

    def mul(self, x, y):
        self.x = x
        self.y = y
        print("x * y = ", x * y)

    def sub(self, x, y):
        self.x = x
        self.y = y
        print("x - y = ", x - y)

    def div(self, x, y):
        self.x = x
        self.y = y
        print("x / y = ", x / y)


c = Calculate()
c.add(2, 3)

#############################################################


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3

# traversing the linked list
current = node1
while current is not None:
    print(current.data, end="->")
    current = current.next

print("None")

# adding  a new node at he beginning
head = node1
new_node = Node(0)
new_node.next = head
head = new_node

current = head
while current is not None:
    print(current.data, end="->")
    current = current.next

print("None")


# adding new node at the end
new_node_end = Node(50)
current = head
while current.next is not None:
    current = current.next

current.next = new_node_end

current = head
while current is not None:
    print(current.data, end="->")
    current = current.next

print("None")

# inserting the new node at perticular position
new_node = Node(25)
current = head
while current is not None and current.data != 20:
    current = current.next

new_node.next = current.next
current.next = new_node

current = head
while current is not None:
    print(current.data, end="->")
    current = current.next

print("None")