#BISMILLAHIR RAHMANIR RAHIM

print()

#Empty set
A={ } #Not a set. It's empty dictionary
print('Empty', A, ':', type(A))
a=set( )
print('Empty', a, ':', type(a), '\n') #Empty set

#Set with elements
b=[34, 'tasnim', 24, 13, 'esha', 94, 45, 18.78, 'israt', 59, 24, 'esha'] #List
c={34, 'tasnim', 24, 13, 'esha', 94, 45, 18.78, 'israt', 59, 24, 'esha'} #Set (Occurance of every element is 1. Repetitive elements are removed)

#Converting from set to list
d=set(b)
print('Conveting from list\n', b, 'to set:\n', d, '\n') #Set elements will bw printed randomly

#Special
e={20.0, 20, '20'} #{float, int, string}
print('Set of elements:\n', e, '\n') #float 20.0==int 20 (same). So (20 or 20.0)-one of them will be printed