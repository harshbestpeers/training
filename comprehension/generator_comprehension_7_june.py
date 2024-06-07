# Generator Comprehensions
"""Generator Comprehensions are very similar to list comprehensions. One
difference between them is that generator comprehensions use circular
brackets whereas list comprehensions use square brackets. The major difference
between them is that generators don't allocate memory for the whole list.
Instead, they generate each value one by one which is why they are memory
efficient."""

# code using generator comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_gen = (var for var in input_list)
for var in output_gen:
    print(var, end=" ")
print("")

# Conditionals in generator Comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_gen = (var for var in input_list if var % 2 == 0)
for var in output_gen:
    print(var, end=" ")
print()

# if else Condition in generator Comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_gen = ("even" if var % 2 == 0 else "odd" for var in input_list)
for var in output_gen:
    print(var, end=" ")
print()
