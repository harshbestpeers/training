# Dictionary Comprehension
# syntax of dictionary comprehension
# dictionary = {key: value for vars in iterable}

# code without dictionary comprehension
square_dict = {}
for num in range(1, 10):
    square_dict[num] = num*num
print(square_dict)

# code with dictionary comprehension
square_dict = {num: num*num for num in range(1, 10)}
print(square_dict)

# convert prices rs to dollar
old_price = {"milk": 70, "coffee": 400, "bread": 20}
rs_to_dollar = 0.012  # 1 rs equal to 0.012 dollar
new_price = {item: value * rs_to_dollar for (item, value) in old_price.items()}
print(new_price)

# If Conditional Dictionary Comprehension
person = {"harsh": 23, "raju": 12, "rajesh": 40, "ravindra": 15}
young_person_dict = {key: value for (key, value) in person.items() if value <= 18}
print(young_person_dict)

# if-else Conditional Dictionary Comprehension
original_dict = {"harsh": 23, "raju": 12, "rajesh": 40, "ravindra": 15}
new_dict = {k: ("you are eligible for vote" if v >= 18 else "not eligible for vote")
            for (k, v) in original_dict.items()}
print(new_dict)

# Nested Dictionary with Two Dictionary Comprehensions
dictionary = {k2: {k1*k2 for k1 in range(1, 10)} for k2 in range(1, 6)}
print(dictionary)