#BISMILLAHIR RAHMANIR RAHIM

print()

'''FUNCIONS'''

#Argument and Return value
def sum_of_values_of_b(c):
    return sum(c['b'].values())

#Argument and No return value
def sum_of_numbers(c):
    print("Sum of '80, 70, 65, 60, 50, 40':", sum(c['numbers']), '\n')

#No argument and Return value
def items_of_b():
    return a['b']

#No argument and No return value
def keys_of_b():
    d=list(a['b'].keys())
    e=''.join(d)
    print("Keys of 'b':", e, '\n')

#Returning more than one value
def swap(x, y):
    x, y= y, x
    return x, y


'''MAIN FUNCION'''

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
        'E': 33
   },
   79.5: 80
}
print("Sum of values of 'b':", sum_of_values_of_b(a), '\n')
sum_of_numbers(a)
print("Items of 'b':", items_of_b(), '\n')
keys_of_b()
print('After swap, (A, B)=', swap(a['b']['A'], a['b']['B']), '\n')


#Default Parameter Value

def my_name(name='Tasnim'): #If no argument is given while calling function, 'Tasnim' will be the argument
    print(name, end=' ')

print('My name is: ', end='')
my_name('Israt')
my_name()
my_name('Esha')
print('\n')