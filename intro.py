

print("Hello World from Python!")
print(2)
print(5+3)
print(True)

# This is a comment
"""
Multiple
Line
Comment
"""

#Creating variables
name = "Luis"
age = 24
last_name = "Renteria"
found = False
another_age = "50"

print(name)
print(last_name)

#Concatenation
#Casting -> convert a data type to another one (e.g. string (str) -> numbers (int) 
# or numbers (int) -> string (str))
concatenation_example = "My name is: " + name + " and I'm " + str(age) + " years old"
print("My name is: " + name + " and I'm " + str(age) + " years old")
print("Did he showed up to the class? " + str(found))
print(100 + int(another_age))
print(concatenation_example)

#The f format
#f"" or f"""""""
print(f"My name is: {name}, and I'm {age} years old!")
print(f"""
My name is {name}
    and this is an example
of a triple double quoted f format
      """)

#The type() function helps us to know the data type of the variables
print(type(name))
print(type(found))
print(type(age))

#Casting
#Helps us to convert different data types
#str() -> convert from any data type to string
#int() -> convert string number to Numeric values
#float() -> convert string number to float type


#input function/method
#is going to allows us to interact with the terminal and pass some values
#input()
#print(input("Enter your name here:"))
#print(type(input("Enter your age here: ")))
#new_age = int(input("Enter a new age:")) #30
#print(new_age + age)

x = int(input("Enter a first value: "))
y = int(input("Enter a second value: "))
print(x+y)