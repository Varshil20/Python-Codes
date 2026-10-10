# Q.1
# Student Marks Dictionary
# Write a Python program to take a student name and marks as input and store them in a dictionary. 
# Display the student name and marks.
n = int(input("How many records you want to enter : "))

d = {}

for i in range(n) :
    name = input("Name : ")
    marks = int(input("Marks : "))

    d[name] = marks

for i in d :
    print(i ,":" ,d[name])

