# list_comprehension
# Syntax of List Comprehension
# [expression for item in list if condition == True]

numbers = [1, 2, 3, 4]
# list comprehension to create new list
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

# code with out list_comprehension
numbers_1 = [1, 2, 3, 4, 5]
square_numbers = []
for num in numbers_1:
    square_numbers.append(num * num)
print(square_numbers)

# code with list_comprehension
numbers_2 = [1, 2, 3, 4, 5]
square_numbers = [num**2 for num in numbers_2]
print(square_numbers)

# Conditionals in List Comprehension
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers_list if num % 2 == 0]
print(even_numbers)

# if...else With List Comprehension
numbers = [1, 2, 3, 4, 5, 6]
even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in numbers]
print(even_odd_list)

# Nested if With List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

# List Comprehension with String
word = "hello, i am harsh patidar"
vowels = "aeiou"
result = [char for char in word if char in vowels]
print(result)

# Nested List Comprehension
multiplication = [[i * j for j in range(1, 6)] for i in range(2, 5)]
print(multiplication)
