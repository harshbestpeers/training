dict_1={
    "name":"harsh",
    "age":23,
    "task":"performe operation",
    "year":2024}

print(dict_1)
print(dict_1["name"])
print(type(dict_1))
print(len(dict_1))

dict_2 = dict(name = "John", age = 36, country = "Norway")
print(dict_2)

#Accessing Items
print(dict_1["age"])
print(dict_1.get("age")) #get value
print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())

if "name" in dict_1: # Check if Key Exists
  print("Yes, 'model' is one of the keys in the thisdict dictionary")   
   
dict_1["color"] = "white" # add elements
print(dict_1)

#C_hange Dictionary Items
dict_1["name"]="patidar"
dict_1.update({"year": 2020}) 
print(dict_1)

#A_dding Items
dict_1["sname"]="patidar"
dict_1.update({"day": "friday"}) 
print(dict_1)

#R_emove Dictionary Items
print(dict_1.pop("sname"))
print(dict_1)
print(dict_1.popitem())

for x in dict_2:
  print(x) 

#nested dictionary
my_family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  },
  "child4" : {
    "name" : "asd",
    "year" : 2012
  }

} 
print(my_family)
print(my_family["child1"]["name"])

#Loop Through Nested Dictionaries
for x, obj in my_family.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])
