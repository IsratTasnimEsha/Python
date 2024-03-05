#BISMILLAHIR RAHMANIR RAHIM

print()

#Printig 1 to 7(break before print)
for i in range(1, 16):
    if i==8:
        break
    print(i)
print()

#Printig 1 to 8(break after print)
for i in range(1, 16):
    print(i)
    if i==8:
        break
print()

#Printig 1 to 8 using for loop with else
for i in range(1, 16):
    if i>=9:
        break
    print(i)
else:
    print('This is inside else of for.') #will not be printed because the code was executed from 1-8
print()