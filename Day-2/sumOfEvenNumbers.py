n = int(input("Enter number : "))

sum = 0

while n != 0 :
    if n % 2 == 0 :
        sum += n

    n -= 1

print("Sum of even number upto n is : ",sum)