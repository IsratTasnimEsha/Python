#BISMILLAHIR RAHMANIR RAHIM

print()

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

#Printing the keys of the dictionary
print('Keys of the dictionary are:\n\n', a.keys(), '\n\n')

#Printing the values of the dictionary
print('Values of the dictionary are:\n\n', a.values(), '\n\n')

#Printing the items of the dictionary [(key, value) for all ccontents]
print('Items of the dictionary are:\n\n', a.items(), '\n\n')

#Printing the dictionary
print('Dictionary:\n\n', a, '\n\n')

#Adding a key in dictionary
a[69.5]=70
print("After adding key '69.5':\n\n", a, '\n\n')

#Updating dictionary (adding a with c)
c={
    'excellent': 'very good',
    'worst': 'so bad',
    'd': {
        64.5: 65,
        59.5: 60,
        49.5: 50
    }
}

#Updating the dictionary (a) by adding dictionary (c)
a.update(c) #a=a+c
print('Updated dictionary:\n\n', a, '\n\n')

#Using dictionary.get(key) [Find if the desired key is present in given dictionary or not]
print("Key: esha\tValue:", a.get('esha'), '\n\n') #Not matched. Will show 'None'
#Using dictionary[key] [It's sure that desired key is present  in given dictionary. Else it is a wrong information]
#print("Key: esha\tValue:", a['esha'], '\n')  //Not matched. Will show error

#Clearing the dictionary
a.clear()
print('After clearing the dictionary:\n\n', a, '\n')