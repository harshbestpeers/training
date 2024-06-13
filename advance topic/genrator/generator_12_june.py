# generator
# Create Python Generator
def generator_name(arg):
    # statements
    yield something


# Example 1
# example of a generator function that produces a sequence of numbers
def my_generator(n):
    value = 0
    while value < n:
        yield value

        value += 1


for value in my_generator(5):
    print(value)


# Example 2
# program using iterator
class PwoTwo:
    def __init__(self, max=0):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.max <= self.n:
            raise StopIteration
        power = 2 ** self.n
        self.n += 1
        return power


power = PwoTwo(4)
for i in PwoTwo(4):
    print(i)

# program using generator
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


for i in PowTwoGen(4):
    print(i)


# example 4
# Multiple generators can be used to pipeline a series of operations.
def fibonacci_number(nums):
    a = 0
    b = 1
    for i in range(nums):
        a, b = b, a + b
        yield a


def square_number(nums):
    for num in nums:
        yield num ** 2


print(sum(square_number(fibonacci_number(10))))
