'''
Mawe Makaratasi Makasi
'''

import random 
import time

ALL_PLAYERS = {
    "Mtu one": {
        "choices":[],
        "wins":[],
        } ,

    "Mtu Two": {
        "choices": [],
        "wins":[]
    },
    
    "Mtu Tatu": {
        "choices": [],
        "wins":[]
    }
    }

RPS=['Mawe', "Makaratasi", "Makasi"]
pre_timer = 3
MaxRounds = 3

players_name = []
for player in ALL_PLAYERS:
    players_name.append(player)

player1 = random.choice(players_name)
player2=''

while len(player2) == 0:
    if random.choice(players_name) != player1:
        player2 = random.choice(players_name)

for round in range(MaxRounds):
    players =[player1, player2]
    print('ROUND: ' + str(round+1))
    for count in range( pre_timer ):
        print("\t" + str(count+1) + " ", end="")
        time.sleep(1)
    print("\tSHOOT!!")
    
    ALL_PLAYERS[player1]["choices"].append( random.choice(RPS) )
    ALL_PLAYERS[player2]["choices"].append( random.choice(RPS) )

    print(f'\n{player1}: {ALL_PLAYERS[player1]["choices"][round]}')
    print(f'{player2}: {ALL_PLAYERS[player2]["choices"][round]}')

    if ALL_PLAYERS[player1]["choices"][round] == "Makaratasi" and ALL_PLAYERS[player2]["choices"][round] =="Mawe":
        ALL_PLAYERS[player1]['wins'].append(1)
        ALL_PLAYERS[player2]['wins'].append(0)
        print(f'{player1}: wins Round: {round + 1}')
    elif ALL_PLAYERS[player1]["choices"][round] == "Makasi" and ALL_PLAYERS[player2]["choices"][round] =="Makaratasi":
        ALL_PLAYERS[player1]['wins'].append(1)
        ALL_PLAYERS[player2]['wins'].append(0)
        print(f'{player1}: wins Round: {round + 1}')
    elif ALL_PLAYERS[player1]["choices"][round] == "Mawe" and ALL_PLAYERS[player2]["choices"][round] =="Makasi":
        ALL_PLAYERS[player1]['wins'].append(1)
        ALL_PLAYERS[player2]['wins'].append(0)
        print(f'{player1}: wins Round: {round + 1}')
    elif ALL_PLAYERS[player1]["choices"][round] == "Makaratasi" and ALL_PLAYERS[player2]["choices"][round] =="Makaratasi":
        ALL_PLAYERS[player1]['wins'].append(0)
        ALL_PLAYERS[player2]['wins'].append(0)
        print(f'{player1}: wins Round: {round + 1}')
    elif ALL_PLAYERS[player1]["choices"][round] == "Makasi" and ALL_PLAYERS[player2]["choices"][round] =="Makasi":
        ALL_PLAYERS[player1]['wins'].append(0)
        ALL_PLAYERS[player2]['wins'].append(0)
        print(f'{player1}: wins Round: {round + 1}')
    elif ALL_PLAYERS[player1]["choices"][round] == "Mawe" and ALL_PLAYERS[player2]["choices"][round] =="Mawe":
        ALL_PLAYERS[player1]['wins'].append(0)
        ALL_PLAYERS[player2]['wins'].append(0)
        print(f'{player1}: wins Round: {round + 1}')
    else:
        ALL_PLAYERS[player1]['wins'].append(0)
        ALL_PLAYERS[player2]['wins'].append(1)
        print(f'{ALL_PLAYERS[player2]}: wins Round: {round + 1}')

    
print ("\nFINAL RESULTS!!!")
print(f'\n{player1}: {ALL_PLAYERS[player1]["wins"]}')
print(f'{player2}: {ALL_PLAYERS[player2]["wins"]}')

totalwin1 =ALL_PLAYERS[player1]["wins"][0] +ALL_PLAYERS[player1]["wins"][1] + ALL_PLAYERS[player1]["wins"][2]
totalwin2 =ALL_PLAYERS[player2]["wins"][0] +ALL_PLAYERS[player2]["wins"][1] + ALL_PLAYERS[player2]["wins"][2]

print(f'{player1} Score: {totalwin1}')
print(f'{player2} Score: {totalwin2}')

if totalwin1 > totalwin2:
    print(f'\n{player1}: WON THE GAME!!\n')
elif totalwin1 == totalwin2:
    print("\nDRAW!!\n")
else:
    print(f'\n{player2}  WON THE GAME!!\n')


       


