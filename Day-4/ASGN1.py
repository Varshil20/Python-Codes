# 1. Find the Sum of All Elements in a Set
# Write a Python program to create a set of integers and calculate the sum of all elements.

a = {10,20,30,20,30,40,40,50}
# set only contain unique element and not contain duplicate element

print(a)
sum = 0

for i in a :
    sum += i

print(sum)