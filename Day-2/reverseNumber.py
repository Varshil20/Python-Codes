n = int(input("Enter number to reverse : "))

reverse = 0

while n != 0 :
    last = n % 10
    reverse = reverse*10 + last
    n //=10

print("Number after reverse is : ",reverse)