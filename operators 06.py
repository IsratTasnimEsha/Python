#BISMILLAHIR RAHMANIR RAHIM

print()

a=5
b=10.5
c=True
d=False
e='esha'
f=[12.10, 2000, "Esha", True]
g='I am doing B.Sc in engineering from Khulna University of Engineering and Technology in Computer Science and Engineering.'

#Arithmetic Operators
print( a, "+", b, "=",a+b)
print( a, "-", b, "=", a-b)
print( a, "*", b, "=", a*b)
print( a, "/", b, "=", a/b, '\n')

#Asignment Operators
a=6
print( "a=", a)
a+=5
print( "a+=", a)
a-=4
print( "a-=", a)
a*=3
print( "a*=", a)
a/=2
print( "a/=", a, '\n')

#Comparison Operators
print( a, "==", b, ":",a==b)
print( a, "!=", b, ":",a!=b)
print( a, ">", b, ":",a>b)
print( a, ">=", b, ":",a>=b)
print( a, "<", b, ":",a<b)
print( a, "<=", b, ":",a<=b, '\n')

#Logical Operators
print('c and d =', c and d)
print('c or d =', c or d)
print('not c =', not c)
print('not d =', not d, '\n')

#Others
print(b, 'to the power 3:', b**3)
import math
print('2 to the power 3:', math.pow(2, 3))
print('sqrt(6):', math.sqrt(6), '\n')
print('Value of pi', math.pi, '\n')
print('gcd of 4 and 6:', math.gcd(4, 6), '\n')
print('factorial of 5:', math.factorial(5), '\n')
print('sin(30):', math.sin(30))
print('cos(30):', math.cos(30))
print('tan(30):', math.tan(30), '\n')
print('ceil(4.8):', math.ceil(4.8))
print('floor(4.8):', math.floor(4.8), '\n')
print('log5:', math.log(5))
print('log10(30):', math.log10(30), '\n')

#is [ (varriable is value) same as (varriable==value) ]
print('c is True:', c is True)
print('d == True:', d == True, '\n')
#print("e is 'esha':", e is 'esha', '\n')  \\Will be printed but with warning. Shouldn't be used. (==) should be used for this type of cases

#is not  [ (varriable is not value) same as (varriable!=value) ]
print('d is not True:', d is not True, '\n')

#in
print('False in f:', False in f)
print("'B.Sc in engineering' in g:", 'B.Sc in engineering' in g, '\n')

#not in
print('12.1 not in f:', 12.1 not in f, '\n')