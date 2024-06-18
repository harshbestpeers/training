# Example 1
# Given a list of elements, sort by K digit in each element.
test_list = [4322, 2122, 123, 1344]
k = 2
sort_list = sorted(test_list, key=lambda ele: str(ele).count(str(k)))
print(sort_list)


# Example 2
""" Given dictionary, perform sort on basis of maximum or minimum element
present in dictionary values list."""

test_dict = {
    "Gfg": [6, 4],
    "is": [10, 3],
    "best": [8, 4],
    "for": [7, 13],
    "geeks": [15, 5],
}
print(sorted(test_dict.items(), key=lambda ele: ele[1]))


# Example 3
# sort dict by values associated with the ‘key’
nested_dict = {"a": {"key": 3}, "b": {"key": 1}, "c": {"key": 2}}
print(sorted(nested_dict.items(), key=lambda ele: ele[1]["key"]))


# Example 4
# Sort dictionary by value list length
test_dict = {"is": [1, 2], "gfg": [3], "best": [1, 3, 4]}
print(sorted(test_dict, key=lambda ele: len(test_dict[ele])))
print(
    {
        key: test_dict[key]
        for key in sorted(test_dict, key=lambda ele: len(test_dict[ele]))
    }
)


# Example 5
# Second largest value in a Python Dictionary
test_dict = {"one": 5, "two": 1, "three": 6, "four": 10}
second_largest = sorted(test_dict, key=lambda ele: test_dict[ele])
print(second_largest[-2])


# Example 6
# Sort Dictionary by Value Difference
test_dict = {
    "gfg": [34, 87],
    "is": [10, 13],
    "best": [19, 27],
    "for": [10, 50],
    "geeks": [15, 45],
}

print(sorted(test_dict.items(), key=lambda ele: abs(ele[1][0] - ele[1][1])))


# Example 7
""""Give a dictionary with value lists, sort the keys by summation of values
in value list."""
test_dict = {"Gfg": [6, 7, 4], "is": [4, 3, 2], "best": [7, 6, 5]}
print(sorted(test_dict.items(), key=lambda ele: sum(i for i in ele[1])))
new_dict = sorted(
    {key: sum(i for i in val) for key, val in test_dict.items()}.items(),
    key=lambda ele: ele[1],
)
print(new_dict)
