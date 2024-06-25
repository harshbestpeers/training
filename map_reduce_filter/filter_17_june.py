# filter() function
# Syntax: filter(function, sequence)


def fun(var):
    letter = ["a", "i", "e", "o", "u"]
    if var in letter:
        return True
    else:
        return False


sequence = ["g", "e", "e", "j", "k", "s", "p", "r"]
result = filter(fun, sequence)
# print(list(result))
for i in result:
    print(i)


# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]
odd = filter(lambda x: x % 2 != 0, seq)
print("odd no.", list(odd))

even = filter(lambda x: x % 2 == 0, seq)
print("even no. ", list(even))


# Filter Function in Python with Lambda and Custom Function
def multiple_of_3(num):
    if num % 3 == 0:
        return True
    else:
        return False


seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = list(filter(lambda x: multiple_of_3(x), seq))
print(result)

# Example 1
"""Write a Python function that filters out all elements less than or equal
than a specified value from a list of numbers using the filter function"""
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = list(filter(lambda x: x <= 10, seq))
print(result)
