# create list
test_list = [4, 7, 0]

# create an iterator
iterator = iter(test_list)

print(next(iterator))  # get first element of the iterator
print(next(iterator))  # get second element of the iterator
print(next(iterator))  # get third element of the iterator

# usig for loop
my_list = [2, 5, 3, 7]
iterator = iter(my_list)
for ele in iterator:
    print(ele)


# Building Custom Iterators'
class PowerTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            return StopIteration


number = PowerTwo(3)
i = iter(number)
print()
print(next(i))
print(next(i))
print(next(i))


# Example 3:
class Test:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.n = 10
        return self

    def __next__(self):
        n = self.n
        if n >= self.limit:
            raise StopIteration
        else:
            self.n = n + 1
        return n


num = Test(15)
for i in Test(15):
    print(i)


# Example 4
class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        char = self.string[self.index]
        self.index += 1
        return char


string = "hello world"
char = StringIterator(string)
for i in char:
    print(i)


# Example 5
class ListItrator:
    def __init__(self, list):
        self.list = list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        char = self.list[self.index]
        self.index += 1
        return char


list = [1, 2, 3, 6, 4, 57, 8, 3, 6, 8, 5, "gtfgbd", "345634"]
char = ListItrator(list)
for i in char:
    print(i, end=" ")
print()
