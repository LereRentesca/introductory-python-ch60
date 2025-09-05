x = int(input("Enter your first value:"))
y = int(input("Enter your second value:"))

#Convencional If-Else
if x == y:
    print("They're the same")
else:
    print("They're different")

#Short hand if-else (Ternary Operators or Conditional Expressions)
print("They're the same") if x == y else print("They're different")