#BISMILLAHIR RAHMANIR RAHIM

print()

#Empty dictionary
A={ }
print('Empty', A, type(A), '\n')

#Dictionary with elements
a= {
    'key': 'value',
    'good': 'well',
    'bad': 'not good',
    'numbers': [80, 70, 65, 60, 50, 40],
    'b': {
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
print("Key: good\tValue:", a['good'])
print("Key: bad\tValue:", a['bad'])
print("Key: numbers\tValue:", a['numbers'])
print("Key: b\tValue:", a['b'])
print("Key: b\tValue:", a['b']['A']) #Printing value of 'A' from dictionary 'b' from main dictionary a
print("Key: 79.5\tValue:", a[79.5], '\n')

#Taking dictionary elements as input
b={ }
b[69.5]=input("Key: 69.5\tValue:")
b[64.5]=input("Key: 64.5\tValue:")
b[59.5]=input("Key: 59.5\tValue:")
b[49.5]=input("Key: 49.5\tValue:")
b[39.5]=input("Key: 39.5\tValue:")
print('\nDictionary:\n', b, '\n')