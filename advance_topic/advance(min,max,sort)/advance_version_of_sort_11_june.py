# advance version of sort function

# Example 1
numbers = [2, 4, 1, 6, 3]
numbers.sort(key=lambda x: x)
print(numbers)


# Example 2
lst = [("Ann", "20", "400"), ("Scott", "40", "500"), ("Bean", "10", "450")]
lst.sort(key=lambda x: x[0])
print(lst)


# Example 3
test_dict = [{"age1": 50}, {"age2": 45}, {"age3": 46}]
test_dict.sort(key=lambda ele: [ele[key] for key in ele])
print(test_dict)


# Example 4
# Sort Dictionary by Value Difference
test_dict = [
    {"gfg": [34, 87]},{"is": [10, 13]},
    {"best": [19, 27]},
    {"for": [10, 50]},
    {"geeks": [15, 45]},
]
test_dict.sort(key=lambda ele: [sum(val for val in ele[key]) for key in ele])
print(test_dict)
