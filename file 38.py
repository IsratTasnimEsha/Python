#BISMILLAHIR RAHMANIR RAHIM

print()

#opening file in write mode and storing file elements in f
f=open('E:\\Programming\\Programs\\.vscode\\Extras\\Text Files\\text_file.txt', 'w')
#writing in file
f.write('''Hii this is Israt Tasnim Esha from Shibpur, Narsingdi.
I am currently in Khulna University of Engineering and Technology.''')
#closing file and making f free
f.close()

#opening file in append mode storing file elements in f
f=open('E:\\Programming\\Programs\\.vscode\\Extras\\Text Files\\text_file.txt', 'a')
#appending in file
f.write('''\nMy department is Computer Science and Engineering.
And my id no. is 1907090.''')
f.close()

f=open('E:\\Programming\\Programs\\.vscode\\Extras\\Text Files\\text_file.txt', 'a')
#writing a line in file f 
f.writelines(['''\nMy college is Dhaka Mohanagar Girls' College.
My id was 182001 there.\n'''])
f.close()

#opening file in read mode storing file elements in f
f=open('E:\\Programming\\Programs\\.vscode\\Extras\\Text Files\\text_file.txt', 'r')
#printing stored data from f
for i in f:
    print(i)
f.close()

f=open('E:\\Programming\\Programs\\.vscode\\Extras\\Text Files\\text_file.txt', 'r')

while True:
    #reading a line each time from a file
    line=f.readline()
    print(line)
    #When there is no remaining line
    if not line:
        break

f.close()

with open('E:\\Programming\\Programs\\.vscode\\Extras\\Text Files\\text_file.txt') as f:
    for i in f:
        #reading each words from a file
        for j in i.split():
            print(j, '\n')
f.close()

with open('E:\\Programming\\Programs\\.vscode\\Extras\\Text Files\\text_file.txt') as f:
    while True:
        #reading a letter each time from a file
        letter=f.read(1)
        print(letter)
        #When there is no remaining line
        if not letter:
            break
f.close()