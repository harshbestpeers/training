str_1="we are performing operation on string"
str_2="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(str_1[0])

for x in str_1: #looping through a string
    print(x,end="")

# length of strings
len_str=len(str_1)
print("len of str:",len_str)

print("string" in str_1) #check sting

if "string" in str_1:
    print("yes, 'string' is present")

print("harsh" not in str_1) #check if not   

#string slicing
print(str_2[2:10])
print(str_1[:50]) #slice from the start
print(str_1[6:]) #slice from the end
print(str_1[-20:-10]) #negetive indexing

# modify string
print(str_1.upper()) #upper case
print(str_1.lower()) #lower case
print(str_1.strip()) #remove white space
print(str_1.replace("w","h")) #replace sring
print(str_1.split()) #split string

#String Concatenation
str_3=str_1+str_2
print(str_3)

#Python - Format - Strings
age=36
text=f'my name is harsh, I am {age} year old'
print(text)
print(f'my name is harsh, i am {4*5} year old')

txt = "We are the so-called \"Vikings\" from the north."

#string methods

print(str_1.capitalize()) #Converts the first character to upper case
print(str_1.casefold())   #Converts string into lower case
print(str_1.center(200))  #Returns a centered string
print(str_1.count("we"))  #Returns the number of times a specified value occurs in a string
print(str_1.endswith("string"))   # Returns true if the string ends with the specified value
print(str_1.find("string"))  #Searches the string for a specified value and returns the position of where it was found
print(str_1.index("string"))  #Searches the string for a specified value and returns the position of where it was found
print(str_1.isalnum())  #Returns True if all characters in the string are alphanumeric
print(str_1.isalpha())  #Returns True if all characters in the string are in the alphabet
print(str_1.isdigit())  #Returns True if all characters in the string are digits
print(str_1.isdecimal())  # Returns True if all characters in the string are decimals
print(str_1.islower())   #Returns True if all characters in the string are lower case
print(str_1.isupper())   
print(str_1.startswith("Hello"))
print(str_1.splitlines())