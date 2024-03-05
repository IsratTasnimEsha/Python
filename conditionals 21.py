#BISMILLAHIR RAHMANIR RAHIM

print()

#if-elif-else ladder

a=[1, 2, 3, 4, 5]
b=[11, 12, 13, 14, 15]
c=[21, 22, 23, 24, 25]
d=[31, 32, 33, 34, 35]
e=[41, 42, 43, 44, 45]
f=34

if f in a:
    print(f'{f} is in list a(index:{a.index(f)}).')

elif f in b:
    print(f'{f} is in list b(index:{b.index(f)}).')

elif f in c:
    print(f'{f} is in list c(index:{c.index(f)}).')

elif f in d:
    print(f'{f} is in list d(index:{d.index(f)}).')

else:
    print(f'{f} is in list e(index:{e.index(f)}).')

print()


#Multiple if statements

g=62

if(g>100):
    print(g, 'is greater than 100.')

if(g>=75):
    print(g, 'is greater than or equal to 75.')

if(g>=50):
    print(g, 'is greater than or equals to 50.')

if(g>25):
    print(g, 'is greater than 25.')
    
elif(g<=25): #elif and else are optional
    print(g, 'is less than or equals to 25.')

print()


#

h=72

i=f'{h} is an even number.' if h%2==0 else f'{h} is an odd number.'
print(i, '\n')