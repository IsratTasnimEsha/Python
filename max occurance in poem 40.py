#BISMILLAHIR RAHMANIR RAHIM

word_dict={ }
c=0
mx=0

with open('E:\\programming\\.vscode\\Text Files\\the_raven.txt', 'r') as f:
    for i in f:
        i=i.strip()
        p=i.split(' ')
        for i in p:
            if i in word_dict:
                word_dict[i].append(i)
            else:
                word_dict[i]=[i]
    
    word_list=list(word_dict.keys())
    count_list=list(word_dict.values())

    for i in range(len(word_dict)):
        #print(word_list[i], len(count_list[i]))
        if len(count_list[i])>mx:
            mx=len(count_list[i])
    
    print('\nMax occurance:', mx, '\n\nWords are:')

    for i in range(len(word_dict)):
        if len(count_list[i])==mx:
            print(3 * ' ', word_list[i])
    print()