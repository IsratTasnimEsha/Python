#BISMILLAHIR RAHMANIR RAHIM

print("\n")

#muliple line string
a='''Israt Tasnim Esha
Roll: 1907090
Subject: CSE'''

#single line string using single quotation
b='Institute: KUET'

#single line string using double quotation
B="Blood Group=A-" #case sensitive

#integer
c=2000

#Printing by changing number systems

#binary
print(c, 'in binary\n', format(c, 'b'))
print('or', bin(c), '\n')

#octal
print(c, 'in octal\n', format(c, 'o'))
print('or', oct(c), '\n')

#decimal
print(c, 'in decimal\n', format(c, 'd'), '\n')

#hexa decimal
print(c, 'in hexa decimal\n', format(c, 'x'))
print('or', hex(c), '\n')


#float
d=12.1454444
D=2.3e-3
print(round(d, 2))
print(round(D, 3), '\n')

#Boolean
e=True
E=False

#None
f=None

#Hexadecimal number
g=0XF

#Complex number
h=3+2j

#Printing the Variables and type of Variables and id no of Variables
print(a, '\n', type(a), '\n', 'Id no.:', id(a), '\n')
print(b, '\n', type(b), '\n', 'Id no.:', id(b), '\n')
print(B, '\n', type(B), '\n', 'Id no.:', id(B), '\n')
print(c, '\n', type(c), '\n', 'Id no.:', id(c), '\n')
print(d, '\n', type(d), '\n', 'Id no.:', id(d), '\n')
print(D, '\n', type(D), '\n', 'Id no.:', id(D), '\n')
print(e, '\n', type(e), '\n', 'Id no.:', id(e), '\n')
print(E, '\n', type(E), '\n', 'Id no.:', id(E), '\n')
print(f, '\n', type(f), '\n', 'Id no.:', id(f), '\n')
print(g, '\n', type(g), '\n', 'Id no.:', id(g), '\n')
print(h, '\n', type(h), '\n', 'Id no.:', id(h), '\n')