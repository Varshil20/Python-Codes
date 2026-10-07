# 2.Find the Maximum Element
# Write a Python program to create a set of integers and find the largest element in the set.

n = int(input("Enter how many elements you want to add to the set: "))
print("Add elements to the set:")

# Initialize empty set correctly
a = set() 
for i in range(n):
    a.add(int(input()))

# Use float('-inf') to handle negative numbers properly
# Also, rename 'max' to 'max_val' so we don't overwrite Python's built-in max() function
max_val = float('-inf') 
print(max_val)

# Iterate directly through the elements in the set 'a'
for element in a:
    if element > max_val:
        max_val = element

print("Max is", max_val)