# 5.Find the Sum of Even Numbers
# Write a Python program to create a set of integers and calculate the sum of only the even numbers.

n = int(input("Enter how many number you want to enter to the set : "))

a = set()

for i in range(n) :
    a.add(int(input()))

evenSum = 0

for i in a :
    if i % 2 == 0 :
       evenSum += i


print("sum of even number of set is ",evenSum)