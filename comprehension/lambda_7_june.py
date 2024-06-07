# lambda function
""" A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one
expression."""
# syntax :- lambda arguments : expression

# Add 10 to argument a, and return the result:
x = lambda a: a + 10
print(x(5))

# Lambda functions can take any number of arguments:
x = lambda a, b, c: a + b + c
print(x(1, 2, 3))

# use lambda inside the function


def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(2)
print(my_doubler(11))

"""we defined a lambda function(upper) to convert a string to its upper case
using upper()."""

str1 = 'Harsh Patidar'
upper = lambda string: string.upper()
print(upper(str1))

# Difference Between Lambda functions and def defined function


def cube(y):
    return y*y*y


lambda_cube = lambda y: y*y*y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))

# Lambda Function with List Comprehension
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())

# Python Lambda Function with if-else
max = lambda a, b: a if a > b else b
print(max(12, 4))
