myset = {"apple", "banana", "cherry", True,1,0}
print(myset)

print(type(myset))
print(len(myset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

#Access Items
for x in myset:
  print(x) 

print("banana" in myset)

#Add Items
myset.add("harsh")
print(myset)

myset.update(thisset)
print(myset)

#remove items
myset.remove("banana")
print(myset)

myset.discard("apple")
print(myset)

myset.pop()
print(myset)

#join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set3=set1.intersection(set2)
print(set3)

set3=set1.difference(set2)
print(set3)

set3=set1.difference_update(set2)
print(set3)

value=123456789
target_element=2
list=[int(digit) for digit in str(value)]
print(list.count(2))