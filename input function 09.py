#BISMILLAHIR RAHMANIR RAHIM

print("\n")

#String as input
a=input("Enter your name: ")
print("type of", a, ":", type(a), '\n')
#or
A=str(input('Enter your name: '))
print("type of", A, ":", type(A), '\n\n')


#Integer as input
b=int(input("Enter your roll: "))
print("type of", b, ":", type(b), '\n')
#or
c=input('Enter your roll: ')
C=int(c)
print("type of", C, ":", type(C), '\n\n')


#float as input
d=float(input("Enter your birthday: "))
print("type of", d, ":", type(d), '\n')
#or
e=input("Enter your birthday: ")
E=float(e)
print("type of", E, ":", type(E), '\n\n')


#list as input
f=list(map(int, input().split()))
print("type of", f, ":", type(f), '\n')