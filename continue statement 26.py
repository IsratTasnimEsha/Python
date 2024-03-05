#BISMILLAHIR RAHMANIR RAHIM

print()

#Printing 8 to 15
for i in range(1, 16):
    if i<=8:
        continue
    print(i)
print()

#Printig 1 to 8 using for loop with else
for i in range(1, 16):
    if i>=8:
        continue
    print(i)
else:
    print('This is inside else of for.') #will be printed because the code was executed successfully. 9-15 are not printed but are in loop
print()