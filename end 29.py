#BISMILLAHIR RAHMANIR RAHIM

print()

'''
    *
  ***
 ****
******
'''
for i in range(4):
    print(' ' * (4-i-1), end=' ') #normally ends with line break. here ends with (' ')
    print('*' * (2*i+1), end=' ')
    print(' ' * (4-i-1))
print()

'''
example:
* * * * *
*         *
*         *
*         *
* * * * *
'''

n=int(input())
for i in range(1, n+1):
    if(i==1 or i==n):
        print('* ' * (n-1), end='')
        print('*')
    else:
        print('*', ' ' * (2*n-5), '*')