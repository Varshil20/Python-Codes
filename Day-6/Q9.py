numbers = (10, 20, 30, 40, 50)

n = int(input("Enter number you want to check in the tuple : "))

if n in numbers:
    print("Element exists in the tuple")
else:
    print("Element does not exist in the tuple")