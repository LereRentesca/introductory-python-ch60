# Python Collections
# A group of data elements in python that allows us to store multiple
# data in a single variable
# lists, tuples, dictionaries, set, array

# 1. Lists - They're used to store multiple items in a single variable
# and they are defined by square brackets []
# Properties: lists are ordered, changeable (or mutable), allow duplicates and they're
#             Index based!
empty_list = []
print(f"Collection data type: {type(empty_list)}")

fruits_list = ["apple","banana","cherry","orange","banana"] # this is a list with default values
#                0        1        2        3        4
print(f"Empty list: {empty_list}")
print(f"List: {fruits_list}")
print(f"Retreiving a value: {fruits_list[3]}")
print(f"List length: {len(fruits_list)}")