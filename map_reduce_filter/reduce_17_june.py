# reduce() function

import operator
import functools
import itertools

lis = [1, 2, 3, 4, 5, 6]
sum = functools.reduce(lambda a, b: a + b, lis)
print(sum)

# print maximum element of list
max_no = functools.reduce(lambda a, b: a if a > b else b, lis)
print(max_no)

# using operator functions
sum_of_list_ele = functools.reduce(operator.add, lis)
print(sum_of_list_ele)

mul_of_list_ele = functools.reduce(operator.mul, lis)
print(mul_of_list_ele)

# reduce() vs accumulate()
# sum of list element using reduce
reduce_sum = functools.reduce(lambda a, b: a + b, lis)
print("sum using reduce : ", reduce_sum)

# sum of list element using accumulate
accumulate_sum = itertools.accumulate(lis, lambda a, b: a + b)
print("sum using reduce : ", list(accumulate_sum))
