#BISMILLAHIR RAHMANIR RAHIM

print('\nRock crushes Scissors.\nScissors cuts Paper.\nPaper covers Rock.\n')
Game=[' ', 'Rock', 'Paper', 'Scissors', 'Rock']
import random

def Game_Win(comp, you):
    if(comp==you):
        print('Tie.\n')
    else:
        if(you==max(comp, you)):
            print('You win!\n')
        else:
            print('You lose :(\n')

while 1:
    computer=random.randint(1, 3)
    you=int(input("Your turn: '1' for 'Rock', '2' for 'Paper', '3' for 'Scissors':"))
    if(you==0 or you>3):
        print('\n')
        exit(0)
    if(you==1 and computer==3):
        you=4
    elif(you==3 and computer==1):
        computer=4    
    print('\nComputer:', Game[computer], '\nYou:', Game[you], '\n')
    Game_Win(computer, you)