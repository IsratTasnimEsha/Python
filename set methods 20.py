#BISMILLAHIR RAHMANIR RAHIM

print()

a={92.4, 14, 68.9, 73, 40, 23.8, 87, 34.1, 55}

#Sum of set
print('Sum of the set:', sum(a), '\n')

#Maximum value of set
print('Maximum value of the set:', max(a), '\n')

#Minimum value of set
print('Minimum value of the set:', min(a), '\n')

b={"Mango", 56.24, "Banana", 15, "Orange", True}
print('Initial set:\n', a, '\n')

c={'Banana', 56.24, 'Esha', 90, 12.10, 'Cherry'}

#Adding an element each time to a set
b.add("Cherry")
b.add("Banana") #Repetitive. So will not be added
b.add("Guava") #Repetitive. So will not be added
b.add(False)
print('After adding elements:\n', b, '\n')

#Adding tuple to a set
d=(10, 12.98)
b.add(d)
print('After adding tuple:\n', b, '\n')

#Length of set
print('Length of set:', len(b), '\n')

#Removing a desired element
#b.remove(10) //Not matched. So will show error
b.remove(15)
print('Set after removing 15:\n', b, '\n')

#Removing random element from set
b.pop()
print('Set after removing random element:\n', b, '\n')

#Union of two sets
#print(b or c) //Wrong way
print('b union c:', b.union(c), '\n')

#Intersection of two sets
#print(b and c) //Wrong way
print('b intersection c:', b.intersection(c), '\n')

#(set1-set2) In set1 but not in set2
print('In b but not in c:', b-c, '\n')
print('In c but not in b:', c-b, '\n')

#Clearing the set
c.clear()
print('After clearing the set c:\n', c, '\n')