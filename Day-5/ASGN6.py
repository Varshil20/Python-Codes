# 6.Find the Square of Each Element
# Write a Python program to create a set of integers and create a new set containing the square of each
# element.

n = int(input("how many numbers you want to enter : "))

print("Enter values to the set ")
a = set()

for i in range(n) :
    a.add(int(input()))

square = set()

for i in a :
    square.add(i*i)

print("Original set : ",a)
print("Square of the set : ",square)
