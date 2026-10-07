def multiplyAll(list) :
    mul = 1
    l = len(list)

    for i in range(l) :
        mul *= list[i] 
    

    return mul


num = int(input("Enter how many number you want to multiply : "))

list = [0]*num

print("Enter numbers : ")

for i in range(num) :
    list[i] = int(input(f"Num {i+1} : "))

print("Multiplication of all numbers is",multiplyAll(list))