#BISMILLAHIR RAHMANIR RAHIM

print()

a=[92, 14, 68, 40, 73, 40, 14, 23, 87, 87, 34, 55]
b=["Mango", "Banana", "Apple", "Pine Apple", "Guava", "Orange"]

#Joinning elements of a string list
print('After joinning elements of list:\n', ''.join(b), '\n')

#Maximum value of a list
print('Maximum value of list a is:', max(a), '\n')
print('Maximum value of list b is:', max(b), '\n')

#Maximum value of a list
print('Minimum value of list a is:', min(a), '\n')
print('Minimum value of list b is:', min(b), '\n')

#Sum of elements of a list
print("Sum of the elements of the list:", sum(a), '\n')

#Replacing elements from a list
a[7: 10]=[45, 65, 33, 53, 44, 94, 53]
print('After repacing index 7 to 9 with [45, 65, 33, 53, 44, 94, 53]:\n', a, '\n')

#Removing duplicates in order
from collections import OrderedDict
a=list(OrderedDict.fromkeys(a))
print('List after removing duplicates in order:\n', a, '\n')

#Sorting a list
#c=a.sort()  \\Doesn't work
a.sort()
print('After sorting the list:\n', a, '\n')

#Reversing a list
#d=a.reverse()  \\Doesn't work
a.reverse()
print('After reversing the list:\n', a, '\n')

#Appending an element in the list (at the end)
a.append(865)
print('After appending an element in the list (at the end):\n', a, '\n')

#Inserting an element in any index of the list
a.insert(2, 531)
print("Inserting 531 in index 2:\n", a, '\n')
a.insert(20, 290)
print("Inserting 290 at the end of the list:\n", a, '\n') #Index no. 19 is not available. So 2 will be inserted at the end of the list

#Removing an element of an index from the list
a.pop() #Removes last element
print('Removing last element from list:\n', a, '\n')
a.pop(3) #Removes element from desired index
print('Removing element from index-3:\n', a, '\n')

#Removing desired element from the list
a.remove(68)
print('Removing 68 from list:\n', a, '\n')

#Counting occurance of desired element 
print('Occurance of 44:', a.count(44), '\n')

#Searching index of desired element from the list
print('Index of 40 in the list:', a.index(40), '\n')

#Clearing the list
a.clear()
print('Clearing the list:\n', a, '\n')