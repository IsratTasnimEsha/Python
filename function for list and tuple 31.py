#BISMILLAHIR RAHMANIR RAHIM

print()

a=[92, 14, 68, 73, 40, 23, 87, 34, 55]
b=(34.7, 94, 24, 13.0, 87, 94, 45.23, 18, 73, 59)

#Call by list

def sum_of_list(a):
    A=sum(a)
    return A

print('Sum_of_list:', sum_of_list(a), '\n')


#Call by tuple

def sum_of_tuple(b):
    B=sum(b)
    return B
    
print('Sum_of_tuple:', sum_of_tuple(b), '\n')


#Call by list and tuple

def average(a, b):
    list_sum=sum(a)
    tuple_sum=sum(b)
    return (list_sum+tuple_sum)/2

print('Average:', average(a, b), '\n')