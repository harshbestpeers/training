my_list = ["apple","banana","cherry","mango","orange"]

print(type(my_list))

print(len(my_list)) #length of list
print(my_list[0])

#Access List Items
print(my_list[0])
print(my_list[-2])
print(my_list[1:5])
print(my_list[-1:-5])

if "apple" in my_list: #if "apple" in my_list:
  print("Yes, 'apple' is in the fruits list") 

#Change Item Value
my_list[1]="blackcurrent"
print(my_list)
my_list[1:3] = ["blackcurrant", "watermelon"]
print(my_list)

print(my_list.insert(2, "watermelon")) #insert items

#Add List Items
my_list.append("orange") #add items to the end
print(my_list)

my_list.insert(1, "orange") #insert iteam at specific index
print(my_list)

list_1 = ["apple", "banana", "cherry"]
list_2 = ["mango", "pineapple", "papaya"]
list_1.extend(list_2)
print(list_1)

# remove items in list
my_list.remove("watermelon")
print(my_list)

my_list.pop(1)
print(my_list)

del my_list[0]
print(my_list)

#Loop Lists
for x in my_list: #for loop
  print(x) 

i = 0
while i < len(my_list): #while loop
  print(my_list[i])
  i = i + 1

newlist = [x for x in my_list if "a" in x]
print(newlist) 

newlist = [x for x in my_list if x != "apple"] 
print(newlist)

print(my_list)
#sort the list
print(my_list.sort()) #accending order
print(my_list.sort(reverse=True))
my_list.reverse()
print(my_list)

#join list
list_1=[1,2,3,4,5,6,2,3,3,2]
list_2=["A","s","d","f","g"]
list_3=list_1+list_2
print(list_3)

print(list_1.count(2))