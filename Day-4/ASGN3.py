# 3. Find the Minimum Element
# Write a Python program to create a set of integers and find the smallest element in the set.

n = int(input("Enter how many elements you want to add to the set: "))
print("Add elements to the set:")

# Initialize empty set correctly
a = set() 
for i in range(n):
    a.add(int(input()))

min_val = min(a)

print("Minimum value in set is ",min_val)