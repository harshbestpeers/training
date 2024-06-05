mytuple = ("apple", "banana", "cherry", "apple", "cherry")

print(type(mytuple))

print(len(mytuple))\

#Access Tuple Items
print(mytuple[0])
print(mytuple[0:3])
print(mytuple[-3:-1])

if "apple" in mytuple: #Check if Item Exists
  print("Yes, 'apple' is in the fruits tuple") 

#update tuple
mytuple= ("apple", "banana", "cherry")
y = list(mytuple)
y[1] = "kiwi"
mytuple = tuple(y)
print(mytuple) 

#delete items
del mytuple
print(mytuple)


#loops in tuple
for x in mytuple:
  print(x) 

i = 0
while i < len(mytuple):
  print(mytuple[i])
  i = i + 1 

#join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 

#multiply tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 

print(mytuple) 