p = int(input("Enter principle amount : "))
r = int(input("Enter rate : "))
t = int(input("Enter time : "))

ci = (p * ((1 + (r/100))**t)) - p

print("Compount interest is : ",ci)