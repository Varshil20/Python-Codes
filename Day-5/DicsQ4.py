# Product Price List
# Write a Python program to take the names and prices of three products and store them in a dictionary. 
# Display all product names and their prices.

d = {}

for i in range(3):
    name = input("Product Name: ")
    price = float(input("Product Price: "))

    d[name] = price

print("\nProduct Price List:")

for name in d:
    print(name, ":", d[name])