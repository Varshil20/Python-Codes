# 9.Find the Product of All Elements
# Write a Python program to create a set of integers and calculate the product of all elements.

n = int(input("How many numbers you want to enter : "))

a = set()
for i in range(n) :
    a.add(int(input()))

prod = 1

for i in a :
    prod *= i


print("Product of all element in set is : ",prod)
