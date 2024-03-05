#BISMILLAHIR RAHMANIR RAHIM

print()

with open('E:\\programming\\.vscode\\Text Files\\scores.csv', 'w') as f:
    f.write('''Rohit, 9\nShakib, 56\nBabar, 56\nRohit, 120\nRohit, 105\nShakib, 78\nRohit, 140
Babar, 45\nRohit, 130\nShakib, 102\nBabar, 5\nShakib, 72\nBabar, 67''')

player_scores={ }

with open('scores.csv', 'r') as f:
    for i in f:
        info=i.split(',')
        player=info[0]
        scores=int(info[1])
        if player in player_scores:
            player_scores[player].append(scores)
        else:
            player_scores[player]=[scores]

player_list=list(player_scores.keys())

for i in range(len(player_list)):
    print(f'''{player_list[i]}:\t\tmin_score={min(player_scores[player_list[i]])},\tmax_score={max(player_scores[player_list[i]])},\taverage={sum(player_scores[player_list[i]])/len(player_scores[player_list[i]])}\n''')