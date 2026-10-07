a = [10,20,30,40]

print(a)

a.append(60)
a.append(70)
a.append(80)
a.append(90)
a.append(60)

print(a)

a.extend([100,200,300])
print(a)


a.clear()
print(a)

a = [10,20,30,40]
a.insert(4,99)
print(a)

#remove() the first mathing element from the but if the elment is not present in the list it will give you the error
a.remove(10)
a.remove(30)
a.extend([33,40,56,60])
a.remove(56)
print(a)

#pop() method remove the element from specific index and return the value
c = a.pop(1)
print(c)

#if no index given it will remove the last element from the table 
c = a.pop()
print(c)

#clear() remove all the element present in the list
a.clear()
print(a)

#index() method give the index of the first matching element from the list
#if no such element found it will give you the error

a = [10,20,30,40]
print(a.index(40))

a.extend([10,10,10,20,20,30])
#count() method count how many times the element occurs in the list
#if no element present it will give you zero
print(a.count(21))


#len(reference) method return the number of element present in the list
print(len(a))

#slicing is used to get a portion from the list
#syntax is listReference[start:stop]
#here stop is not included
print(a)
print(a[:20])

#sort() method sort the original list
a.sort()
print(a)

#sorted method create the new sorted list
b = sorted(a)
print(b)