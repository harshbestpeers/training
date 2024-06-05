str_1="we are performing operation on string"
str_2="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(str_1[0])

for x in str_1: #looping through a string
    print(x,end="")

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
print(str_1.casefold())
print(str_1.center(200))  
print(str_1.count("we"))
print(str_1.endswith("string"))  
print(str_1.find("string"))
print(str_1.index("string")) 
print(str_1.isalnum())
print(str_1.isalpha())  
print(str_1.isdigit())
print(str_1.isdecimal())
print(str_1.islower())   
print(str_1.isupper())
