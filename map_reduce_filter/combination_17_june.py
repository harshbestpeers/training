import functools
from functools import reduce
from collections import defaultdict

# Example 1
"""If the given input is an array of numbers, return the sum of all the
positives ones. If the array is empty or there aren't any positive numbers,
return 0."""
seq = [1, -4, 12, 0, -3, 29, -150]
print(functools.reduce(lambda a, b: a + b, list(filter(lambda x: x > 0, seq))))

# example 2
"""Calculate the mean and median values of the number elements from the
input array."""
list_seq = [12, 46, 32, 64]
print(list_seq)

n = len(list_seq)

print("mean : ", functools.reduce(lambda a, b: a + b, list_seq) / len(list_seq))

list_seq.sort()
print(list_seq)
print(
    "median : ",
    [
        (list_seq[n // 2 - 1] + list_seq[n // 2]) / 2
        if n % 2 == 0
        else list_seq[n // 2 - 1]
    ],
)

# Example 3
""" The given input is a string of multiple words with a single space between
each of them. Abbreviate the name and return the name initials."""
string = "George Raymond Richard Martin"
str_list = string.split(" ")
result = functools.reduce(lambda a, b: a + b, [char[0] for char in str_list])
print(result)


# Example 4
"""Devs like to abbreviate everything: k8s means Kubernetes, a11y means
accessibility, l10n means localization. You get the Dev numeronyms by taking
the first and the last letter and counting the number of letters in between.
Words that have less than 4 letters aren't abbreviated, because that would
just be odd. The input is a sentence, and you should abbreviate every word
that is 4 letters long or longer. There won't be any punctuation in the
sentence. g2d l2k e6e"""

string = "Every developer likes to mix kubernetes and javascript"
str_list = string.split(" ")
result = map(lambda x: x[0] + str(len(x) - 2) + x[-1] if len(x) > 4 else x, str_list)

print((" ").join(list(result)))


# Example
"""
If the given input is a number, you should return the factorial of that number.
The factorial of a natural number n is the product of the positive integers
less than or equal to n. So, 2! = 2, 3! = 6, 4! = 24 and so on."""

n = 5
result = functools.reduce(
    lambda a, b: a * b, map(lambda x: x, [i for i in range(1, n + 1)])
)
print(result)


# example`.`
""" Count the occurrences of distinct elements in the given 2D array. The
given input is an array, the elements of which are arrays of strings. The
result is an object whose property names are the values from the arrays and
their value is the number of their occurrences."""

array = [["a", "b", "c"], ["c", "d", "f"], ["d", "f", "g"]]

single_list = reduce(lambda x, y: x + y, array)
print(single_list)
counts = reduce(
    lambda acc, element: {**acc, element: acc.get(element, 0) + 1}, single_list, {}
)
print(counts)


# Example 7
"""You are given an array of objects representing a group of students, each
with a name and an array of test scores. Your task is to use map, filter, and
reduce to calculate the average test score for each student, and then return
an array of objects containing only the students who have an average score
above 90."""

students = [
    {"name": "Alice", "scores": [90, 85, 92]},
    {"name": "Bob", "scores": [75, 80, 85]},
    {"name": "Charlie", "scores": [90, 95, 85]},
    {"name": "Jack", "scores": [100, 100, 100]},
]


def claculate_avg(student):
    score = student["scores"]
    avg = sum(score) / len(score)
    return {"name": student["name"], "avg_scores": avg}


student_avg = list(map(claculate_avg, students))
print(student_avg)

top_students = list(filter(lambda x: x["avg_scores"] > 90, student_avg))
print(top_students)

result = [{"name": i["name"], "avg_score": i["avg_scores"]} for i in top_students]
print(result)


# Example 8
"""You are given an array of objects representing a collection of employees,
each with a name, salary, and department. Your task is to use map, filter,
and reduce to calculate the average salary for each department and then return
an array of objects containing only the departments that have an average
salary above 65000"""


employees = [
    {"name": "Alice", "salary": 60000, "department": "HR"},
    {"name": "Bob", "salary": 75000, "department": "Engineering"},
    {"name": "Charlie", "salary": 80000, "department": "Engineering"},
    {"name": "David", "salary": 70000, "department": "HR"},
    {"name": "Eve", "salary": 50000, "department": "Marketing"},
]

emp_dict = defaultdict(list)

for i in employees:
    emp_dict[i["department"]].append(i["salary"])


def func(data):
    avg = sum(data[1])
    return {"department": data[0], "avg_salary": avg}


avg_salary = list(map(func, emp_dict.items()))
print(avg_salary)

result = filter(lambda x: x["avg_salary"] > 65000, avg_salary)
print(list(result))
