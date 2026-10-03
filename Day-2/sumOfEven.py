n = int(input("Enter the number : "))

sum = 0

while n != 0 :
    last = n % 10

    if last % 2 == 0 :
        sum += last
    
    n //= 10


print("Sum of even digit is : ",sum)

