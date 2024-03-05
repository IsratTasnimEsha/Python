#BISMILLAHIR RAHMANIR RAHIM

print()

#Printing elements of a list using while loop
a=[12.10, 2000, "Esha", True]
print('Printing elements of a list using while loop:')
i=0
while i<len(a):
    print(a[i])
    i=i+1
print()

#Printing elements of a string using while loop
b='Myself Israt Tasnim Esha.'
print('Printing elements of a string using while loop:')
i=0
while i<len(b):
    print(b[i])
    i=i+1
print()

#Printing elements of a tuple using while loop
c=(True, 94.78, 'esha', True, 87, 94.78, False, '73', 87)
print('Printing elements of a tuple using while loop:')
i=0
while i<len(c):
    print(c[i])
    i=i+1
print()

#Printing items of a dictionary using while loop
d= {
    'key': 'value',
    'good': 'well',
    'bad': 'not good',
    'numbers': [80, 70, 65, 60, 50, 40],
    'e': {
        'A+': 80,
        'A': 70,
        'A-': 65,
        'B': 60,
        'C': 50,
        'D': 40,
        'F': 'Fail'
   },
   79.5: 80
}
print('Printing items of a dictionary using while loop:')
f=list(d.items())
i=0
while i<len(f):
    print(f[i])
    i+=1
print()

#Printing elements of a set using while loop
g=(True, 94.78, 'esha', True, 87, 94.78, False, '73', 87)
print('Printing elements of a tuple using while loop:')
i=0
while i<len(g):
    print(g[i])
    i=i+1
print()