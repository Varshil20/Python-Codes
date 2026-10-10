# Q.2
# Employee Salary Record
# Write a Python program to take an employee ID and salary as input and store them in a dictionary. 
# Display the employee ID and salary.

n = int(input("Enter how many records you want to enter : "))

d = {}


for i in range(n) :
    id = int(input("Eid : "))
    salary = int(input("Salary : "))

    d[id] = salary

for i in d :
    print(i , ":",d[i]) 

