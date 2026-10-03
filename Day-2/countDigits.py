n = int(input("Enter the number : "))

digits = 0

while n != 0 :
    n //= 10
    digits += 1

print("Total digits in the number is : ",digits)