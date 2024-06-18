# Set Comprehensions
"""Set comprehensions are pretty similar to list comprehensions. The only
difference between   them is that set comprehensions use curly brackets { }"""

# code with set_comprehension
numbers = [1, 2, 3, 4, 5]
square_numbers = {num**2 for num in numbers}
print(square_numbers)

# conditional in set_comprehensions
# Checking Even number Without using set comprehension
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, 4, 5, 6, 4]
output_set = set()
for i in input_list:
    if i % 2 == 0:
        output_set.add(i)
print("output set using for loop", output_set)

# Checking Even number With using set comprehension
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, 4, 5, 6, 4]
output_set = {var for var in input_list if var % 2 == 0}
print("output set using set comprehension", output_set)

# if else condition using set comprehension
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, 4, 5, 6, 4]
output_set = {"even" if var % 2 == 0 else "odd" for var in input_list}
print(output_set)

# Nested set_comprehensions
output_set = set()
output_set = {frozenset(var * i for var in range(1, 10)) for i in range(1, 6)}
print(output_set)
