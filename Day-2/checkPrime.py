n = int(input("Enter the number : "))

isPrime = True

for i in range(2 , n) :
    if i*i > n :
        break
        
    if n % i == 0 :
        isPrime = False
        break

if isPrime :
    print(n,"is prime number")
else :
    print(n,"is not prime number")