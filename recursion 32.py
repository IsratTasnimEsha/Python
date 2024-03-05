#BISMILLAHIR RAHMANIR RAHIM

print()

def sum_of_first_n_natural_numbers (n):
    if n==0 or n==1:
        return 1
    return n+sum_of_first_n_natural_numbers(n-1)

a=int(input())
print(f'Sum of first {a} natural_numbers is: {sum_of_first_n_natural_numbers(a)}', '\n')