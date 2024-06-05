dict1={
    "name":"harsh",
    "age":23,
    "task":"performe operation",
    "year":2024}

print(dict1)
print(dict1["name"])
print(type(dict1))
print(len(dict1))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Accessing Items
print(dict1["age"])
print(dict1.get("age")) #get value
print(dict1.keys())
print(dict1.values())
print(dict1.items())

if "name" in dict1: # Check if Key Exists
  print("Yes, 'model' is one of the keys in the thisdict dictionary")   
   
dict1["color"] = "white" # add elements
print(dict1)

#Change Dictionary Items
dict1["name"]="patidar"
dict1.update({"year": 2020}) 
print(dict1)

#Adding Items
dict1["sname"]="patidar"
dict1.update({"day": "friday"}) 
print(dict1)

#Remove Dictionary Items
print(dict1.pop("sname"))
print(dict1)
print(dict1.popitem())

for x in thisdict:
  print(x) 

#nested dictionary
myfamily = {
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

} 
print(myfamily)
print(myfamily["child1"]["name"])

#Loop Through Nested Dictionaries
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
