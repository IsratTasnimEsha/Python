#BISMILLAHIR RAHMANIR RAHIM

print()

#Not using string because of sum(tuple)
a=(34.7, 94, 24, 13.0, 87, 94, 45.23, 18, 99.57, 73, 59)
#a=(34.7, 94, '24', 13.0, 87, '94', 45.23, 18, '73', 59) \\sum(tuple) will show error beacause string can't br added with int/float

#Sum of elements of a tuple
print("Sum of the elements of the tuple:", sum(a), '\n')

#Maximum value of a tuple
print("Maximum value of the tuple:", max(a), '\n')

#Minimum value of a tuple
print("Minimum value of the tuple:", min(a), '\n')


#Using string
b=(34.7, 94, '24', 13.0, 87, 94, '45.23', 18, 99.57, '73', 59)

#Counting occurance of desired element 
print('Occurance of 94:', b.count(94), '\n')

#Searching index of desired element from the tuple
print('Index of 13 in the tuple:', b.index(13), '\n') #float 13.0==int 13