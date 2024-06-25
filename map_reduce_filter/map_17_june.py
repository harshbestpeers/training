# Python map() Function Syntax
# Syntax: map(fun, iter)


def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# map() with Lambda Expressions
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


# Add Two Lists Using map and lambda
list_1 = [1, 3, 4, 6]
list_2 = [11, 34, 54, 18, 23]
result = map(lambda x, y: x + y, list_1, list_2)
print(list(result))


# Modify the String using map()
string = ("harsh", "patidar")
result = map(list, string)
print(list(result))


# if-else Statement with map()
# define a function double the even no. and odd is same
def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
result = list(map(double_even, number))
print(result)


# Example 1
"""Write a  Python program to triple all numbers in a given list of integers.
Use Python map."""
number = []
for i in range(100):
    number.append(i)

result = list(map(lambda x: x * 3, number))
print(result)

# example 2
"""Write a Python program to create a list containing the power of said number
in bases raised to the corresponding number in the index using Python map."""
bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(pow, bases_num, index))
print(result)


# Example 3
""" Write a Python program to convert all the characters into uppercase and
lowercase and eliminate duplicate letters from a given sequence. Use the map()
function. """


def change_case(char):
    return char.upper(), char.lower()


string = {"a", "b", "E", "f", "a", "i", "o", "U", "a"}
result = list(map(change_case, string))
print(result)

# Example 4
"""Write a Python program to compute the square of the first N Fibonacci
numbers, using the map function and generate a list of the numbers."""


def fibonacci(n, x=0, y=1):
    for i in range(n):
        yield x
        x, y = y, x + y


n = 10
fab = list(fibonacci(n))
square_fibonacci = list(map(lambda x: x ** 2, fab))
print(square_fibonacci)


# Example 5
"""Write a Python program to compute the sum of elements of an list of
integers. Use the map() function. """
numbers = [1, 2, 3, 4, 5]
result = map(sum, [numbers])
total_sum = list(result)[0]
print("Sum of elements:", total_sum)
