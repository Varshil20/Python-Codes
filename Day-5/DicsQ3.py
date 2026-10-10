# Phone Book
# Write a Python program to take a person's name and phone number as input and store them in a dictionary.
# Ask the user for a name and display the corresponding phone number.

n = int(input("Enter how many records you want to enter : "))

d = {}


for i in range(n) :
    name = input("Name : ")
    number = input("Number : ")

    d[name] = number

name = input("Enter name to get phone number : ")
print("Number for this name is : ",d[name])