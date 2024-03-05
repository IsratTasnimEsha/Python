#BISMILLAHIR RAHMANIR RAHIM

print()

print(range(10))
print(list(range(10)), '\n')

#Printig 0 to 14
for i in range(15): #Means for i in range(0, 15)
    print(i)
print()

#Printig 1 to 15
for i in range(1, 16):
    print(i)
print()

#Difference of successive elements=3
for i in range(1, 16, 3):
    print(i)
print()

#for loop with else(else of for will be printed after the work of for loop is completed )
for i in range(1, 16, 3):
    print(i)
else:
    print('This is inside else of for.')
print()