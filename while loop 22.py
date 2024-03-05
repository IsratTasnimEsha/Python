#BISMILLAHIR RAHMANIR RAHIM

print()

#while i<10:  //Code will run
#    print('Yes')  //Unlimited 'Yes' will be prited beacause 1 is always smaller than 10

i=1
while i>10:
    print('No') #Will print nothing because  1 is always smaller than 10

i=1
while 0:
    print('No')  #Will print nothing because here (while 0:) means condition is always False

#while 1:  //Code will run
#    print('Yes')  //Unlimited 'Yes' will be printed beacause here (while 1:) means condition is always True

#while -1:  //Code will run
    #print('Yes')  //Unlimited 'Yes' will be printed beacause every number except 0 means True

i=1
while i<=10:
    #print('Yes ' + i)  \\int can't be added with string
    print('Yes ' + str(i))
    #i++ \\Wrong syntex
    i+=1
print()

i=1
while i<=10:
    print(i)
    i+=1
else:
    print('This is inside else of while.')
print()