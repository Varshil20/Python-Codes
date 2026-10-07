# 4. Calculate the Average of Set Elements
# Write a Python program to create a set of integers and calculate the average of all elements.

n = int(input("Enter how many elements you want to add to the set: "))
print("Add elements to the set:")

# Initialize empty set correctly
a = set() 
for i in range(n):
    a.add(int(input()))


avg_set = sum(a) / len(a)

print("average value of set is ",avg_set)