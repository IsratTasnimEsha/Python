#BISMILLAHIR RAHMANIR RAHIM

print('\n')

#String Concating
a='Israt '
b="Tasnim "
c='''Esha'''
d=a+b+c
print(d, "\n")


'''
** [m:n]
** m=stating index
** n=ending index+1
** m=empty means index 0
** n=empty means last index+1
'''

#String Slicing (Positive Indices)
print("String from first(0)-4 index:", d[:5])
print("String from 6-11 index:", d[6:12])
print("String from 13-last(16) index:", d[13:], '\n')

#String Slicing (Negative Indices)
print("String without last 2 indices:", d[:-2])
print("String from 6-11 index:", d[-11:-5])
print("String of last 3 characters:", d[-3:], '\n')