#BISMILLAHIR RAHMANIR RAHIM

print()

a='          myself Israt Tasnim Esha. I am doing B.Sc in engineering from Khulna University of Engineering and Technology in Computer Science and Engineering.       '

#Character with maximum ascii value of the string
print('Character with maximum ascii value of the string:', ascii(max(a)), '\n')

#Character with minimum ascii value of the string
print('Character with minimum ascii value of the string:', ascii(min(a)), '\n') #space

#Removing extra spaces from start and end side
#a.strip()  \\Will not work while printing
a=a.strip()
print('String after removing extra spaces from start and end side:\n', a, '\n')

#Length of string
b=len(a)
print("Length of the string:", b, '\n')

#If string starts with desired string or not
print("The string starts with (r) :", a.startswith("r")) #using character
print("The string starts with (myself Israt) :", a.startswith("myself Israt"), '\n') #using string

#If string ends with desired string or not
print("The string ends with (.) :", a.endswith(".")) #using character
print("The string ends with (Computer Science and Engineering.) :", a.endswith("Computer Science and Engineering."), '\n') #using string

#Counting occurance of desired string 
print("Occurance of  'a' in this string:", a.count('a')) #using character
print("Occurance of  'Engineering' in this string:", a.count('Engineering'), '\n') #using string

#Capitalizing first character of a string and uncapitalizing others
#a.capitalize()  \\Will not work while printing
b=a.capitalize() #Permanently changing main string. Otherwise use another variable 
print("String after cpitalization:\n", b, '\n')

#Finding index of desired string(first occurance and first character)
#Using find() [Find if the desired string is present in given string or not]
print("Index of 'E' (first character of 'Engineering'):", a.find('Engineering')) #first occurance only
print("Index of 'n' (first character of 'niaj'):", a.find('niaj')) #Not matched. Will show index (-1)
#or using index() [It's sure that desired string is present  in given string. Else it is a wrong information]
print("Index of 'i' (first character of 'israt'):", a.index('Israt'), '\n')
#print("Index of 'n' (first character of 'noor'):", a.index('noor'))  //Not matched. Will show error

#Replacing one string with another (every occurance will be replaced)
#a.replace('khulna university of engineering and technology', 'MIT')  \\Will not work while printing
a=a.replace('Khulna University of Engineering and Technology', 'MIT') #Permanently changing main string. Otherwise use another variable 
print("Afer replacing 'Khulna University of Engineering and Technology' with 'MIT':\n", a, '\n')

#String in lowercase
b=a.lower()
print('String in lowercase:\n', b, '\n')

#String in uppercase
b=a.upper()
print('String in uppercase:\n', b, '\n')

#Reversing a string
a=a[ : :-1]
print("Reverse string of given string:\n", a, '\n')

#Sorting characters in a string
a=sorted(a)
print("Sorting characters as character list:\n", a, '\n') #As character list
b=''.join(a)
print("Sorting characters as string\n", b, '\n') #As string

#String characters and length are fixed. Full string should be chaged. Otherwise changing character or length is not possible
#a[4]='d' //Not possible