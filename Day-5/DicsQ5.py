# Dictionary Update
# Write a Python program to create a dictionary containing three key-value pairs. 
# Ask the user for a key and a new value, then update the dictionary with the new value. 
# Display the updated dictionary.

d = {
    "name": "Rahul",
    "age": 21,
    "city": "Pune"
}

key = input("Enter key to update: ")
value = input("Enter new value: ")

d[key] = value

print("Updated Dictionary:")
print(d)