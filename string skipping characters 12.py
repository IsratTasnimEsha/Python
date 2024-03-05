#BISMILLAHIR RAHMANIR RAHIM

print('\n')


'''
** [m:n:p]
** m=stating index
** n=ending index+1
** m=empty means index 0
** n=empty means last index+1
**p=(p-1) character will be skipped each time
**p=empty means no character will be skipped
'''

a='We all know that slow and steady wins the race.'

#Skipping characters
print('Skipping 3 characters each time from whole string:\n', a[ : : 4], '\n')
print('Skipping 2 characters each time from 0-10 index:\n', a[ :11:3], '\n')
print('Skipping 1 character each time from 10-17 index:\n', a[10:18:2], '\n')
print('Skipping no character each time from 4-15 index:\n', a[4:16:1], '\n')

#Reversing string and skipping characters
print("Reversing string from 1-19 index and skipping 3 characters each time: ", a[19:0:-3], '\n')
print("Reversing string from 0-10 index and skipping 2 characters each time: ", a[10::-2], '\n')
print("Reversing string from 1-last index and skipping 1 character each time: ", a[:0:-1], '\n')
print("Reversing whole string and skipping no character: ", a[ : : -1], '\n')