# simple function
def my_function():
   print("This is my function")

def other_function():
    print("This is another function")

my_function() #calling function
other_function()

print("-------------")

# function with parameters
def print_full_name(fname, last_name):
    print("This name is: {fname} {last_name}")

# function that return something
def get_full_name(fname, last_name):
    return f"{fname} {last_name}"

# store the returned value in a variable
full_name = get_full_name("Leo", "Flores")
print(full_name)

def subtract(x, y):
    return x-y

res = subtract(1, 3)
print(res)