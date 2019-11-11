"""
MAIN GAME MODULE.
ALL THE GAME PROCESSES ARE PLACED HERE.
ALL THE FUNCTIONS CHECKIGS ARE PLASED HERE TOO (FOR NOW).
"""

import basecharacter as bc
import battlemode as bm
import random
#import undeadcharacters as udc
#import humancharacters as huc
#import beastcharacters as bec
"""
possible_choice = {1: 'Undead', 2: 'Humans', 3: 'Beasts'}
#Choose Fraction
print("What fraction do you want to choose for battle?")
print("Please, put a number: 1 - Undead; 2 - Humans; 3 - Beasts")
answer = int(input())
chosen_fraction = possible_choice[answer]

#kinda menu
print('So, you chose {}, good choice!'.format(chosen_fraction))
player_team = bm.comand_init(chosen_fraction)
print('Your team is:', end = ' ')
for unit in player_team: print(unit.name, end ='   ')
print('\n')
enemy_team = bm.random_enemy_team(chosen_fraction)
print('Enemy team is: ', end = ' ')
for unit in enemy_team: print(unit.name, end = '   ')
print('\n')
"""
player_team = bm.comand_init('Undead')
enemy_team = bm.comand_init('Humans')
bm.Auto_Battle(player_team, enemy_team)
print('\n')
print('It was Undead VS Humans','\n')
player_team = bm.comand_init('Undead')
enemy_team = bm.comand_init('Beasts')
bm.Auto_Battle(player_team, enemy_team)
print('\n','It was Undead VS Beasts','\n')
