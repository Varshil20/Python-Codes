n = int(input("Enter the number : "))

pow = 2

while pow <= n :
    if pow * 2 <= n :
        pow *= 2
    else :
        break


print(pow)