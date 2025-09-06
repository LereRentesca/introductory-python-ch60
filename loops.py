# Loops: for and while
# Is used for iterating over a sequence (or collections like list, tuples,
# dictionaries, set, strings)
# keywords -> continue - jumps to the next iterations and break - finish the loop
# For: for iterating through collections, or iterate in order
# While: iterating until a condition is met

students = ["Reggie", "Zane", "Luis", "Giancarlo", "Kevin"]
found = False
iteration = 0
while not found: # True -> False
    #print(iteration)
    if students[iteration] == "Kevin": # students[0] == "Reggie" -> True
        found = True 
        #print(f"Hey {students[iteration]} is here!")
    else:
        iteration+=1


fruits_list = ["apple","banana","cherry","orange","banana"]

# for fruit in fruits_list:
#     if fruit == "banana":
#         break
#     else:
#         print(fruit)

#Range function - Allow us to iterate through a start, stop and step values
# start it's INLCUSIVE
# stop it's EXCLUSIVE
# step are the increments (e.g. by 1, 2, 3 ... n)

for x in range(10):  #using range with the stop parameter only 
    print(x)

for x in range(5,10,1):
    print(x)

for x in range(0,len(fruits_list),1):
    print(fruits_list[x])

name = "Luis"

for x in name:
    print(x)