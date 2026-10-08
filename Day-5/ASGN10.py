# Write a Python program to create two sets and display the common elements that are even numbers.
# Sample Input:
# Set 1 = {2, 3, 4, 5, 12, 35}
# Set 2 = {1,2,5,4,6,12}
# Sample Output:
# 2
# 4
# 12


set1 = {2, 3, 4, 5, 12, 35}
set2 = {1, 2, 5, 4, 6, 12}

common = set1.intersection(set2)

for num in common:
    if num % 2 == 0:
        print(num)