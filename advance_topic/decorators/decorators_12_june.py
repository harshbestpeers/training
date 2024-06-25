# Decorator
# Treating the functions as objects.
def name(txt):
    return txt.upper()


print(name("harsh"))
new = name
print(new("harsh"))


#  Passing the function as an argument
def upper(txt):
    return txt.upper()


def lower(txt):
    return txt.lower()


def greet(func):
    val = func("hello my dear friends")
    print(val)


greet(upper)
greet(lower)


#  Returning functions from another function
def adder(x):
    def inner(y):
        return x + y

    return inner


add = adder(10)
print(add(20))

# now we learn decorator
"""As stated above the decorators are used to modify the behaviour of function
or class. In Decorators, functions are taken as the argument into another
function and then called inside the wrapper function."""


# Example 1
def Decorators(func):
    def wrapper():
        print("transaction initiated")
        func()
        print("transaction completed")

    return wrapper


@Decorators
def hello():
    print("... execute all the step")


hello()
# val = Decorators(hello)
# val()


# Example 2
def make_pretty(func):
    def inner():
        print("i am decorator")
        func()

    return inner


@make_pretty
def ordinary():
    print("i am ordinary")


ordinary()


# Example 3
def smart_divide(func):
    def inner(a, b):
        print("i am going to divide", a, "and", b)
        if b == 0:
            print("oops...")
            return
        else:
            func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(2, 5)
divide(9, 2)


# Example 4
def divide(func):
    def inner(a, b):
        print("i am going to divide", a, "and", b)
        if b == 0:
            print("oops")
            return
        else:

            func(a, b)
        print("divide is done")

    return inner


def sum(func):
    def inner(a, b):
        print("i am going to sum", a, "and", b)
        func(a, b)
        print("sum is done")

    return inner


@divide
@sum
def hello(a, b):
    print(a / b)


hello(1, 2)


# Example 5
def upper(func):
    def inner():
        print("txt before upper")
        b = func()
        print(b.upper())

    return inner


@upper
def text():
    a = input("")
    return a


text()


# creating decorater inside the class
class A:
    def decorater(func):
        def innner(self):
            print("decorater start")
            func(self)
            print("decorater end")

        return innner

    @decorater
    def func1(self):
        print("dacorating class A")


class B(A):
    @A.decorater
    def func2(self):
        print("decorating class B")


obj = B()
obj.func1()
obj.func2()
