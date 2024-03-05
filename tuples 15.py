#BISMILLAHIR RAHMANIR RAHIM

print()

#Empty touple
a=( )
print('a=( ): \n', type(a), '\n')

#Touple with only one element
B=(71)  #It's not a touple
print('B=(71): \n', type(B), '\n')
b=(34, )
print('b=(34, ): \n', type(b), '\n')

#Touple with more than one elements
c=(True, 94.78, 'esha', True, 87, 94.78, False, '73', 87)
print("c=(True, 94.78, 'esha', True, 87, 94.78, False, '73', 87): \n", type(c), '\n')

#Printing an element from touple
print('Element of index-4:', c[4], '\n')

#Elements and length of a touple can't be changed.
#a[0]=87 //Not possible
#c[3]="tasnim"  //Not possible