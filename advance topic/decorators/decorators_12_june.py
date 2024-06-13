# Decorator

# Example 1
def Decorators(func):
    def wrapper():
        print("transaction initiated")
        func()
        print("transaction completed")
    return wrapper

@ Decorators
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

@ make_pretty
def ordinary():
    print("i am ordinary")

ordinary()


# Example 3
def smart_divide(func):
    def inner(a,b):
        print("i am going to divide",a,"and",b)
        if (b==0):
            print("oops...")
            return
        else:
            func(a,b)
    return inner

@ smart_divide
def divide(a,b):
    print(a/b)

divide(2,5)
divide(9,2)
