#BISMILLAHIR RAHMANIR RAHIM

print('\n1. Registration\n2. Login\n')
enter=input()

if enter=='1':
    with open('E:\\programming\\.vscode\\Text Files\\user_login.txt', 'w') as login:
        username=login.write(input('\nEnter Username: '))
        login.write(' ')
        password=login.write(input('\nEnter Password: '))
        print()

if enter=='2':
    with open('E:\\programming\\.vscode\\Text Files\\user_login.txt', 'r') as login:
        for i in login:
            p=i.split(' ')
        correct_username=False
        while not correct_username:
            user_name=input('\nEnter Username: ')
            if user_name==p[0]:
                correct_password=False
                while not correct_password:
                    _password=input('\nEnter Password: ')
                    if _password==p[1]:
                        print('\nWelcome to cricket!!!\n\n1. Scores.\n2. Exit.\n')
                        enter2=input()
                        if enter2=='1':
                            with open('E:\\programming\\.vscode\\Text Files\\scores.csv', 'r') as f:
                                for i in f:
                                    print('\n', i)
                                break
                            break
                        elif enter2=='0':
                            exit(0)
                        exit(0)
                    else:
                        print('\nPassword is wrong. Please try again.\n')
            else:
                print('\nNo usernmae mathched. Please try again.\n')