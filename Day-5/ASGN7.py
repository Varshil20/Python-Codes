# 7.Add Corresponding Elements from Two Sets
# Write a Python program to create two sets containing the same number of elements. Convert them into 
# lists and calculate the sum of corresponding elements.
# Sample Input:
# Set 1 = {10, 20, 30}
# Set 2 = {1, 2, 3}
# Sample Output:
# 11
# 22
# 33

set1 = {10, 20, 30}
set2 = {1, 2, 3}

list1 = list(set1)
list2 = list(set2)

for i in range(len(list1)):
    print(list1[i] + list2[i])