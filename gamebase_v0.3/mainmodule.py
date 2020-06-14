"""
MAIN GAME MODULE.
ALL THE GAME PROCESSES ARE PLACED HERE.
ALL THE FUNCTIONS CHECKIGS ARE PLASED HERE TOO (FOR NOW).
"""

import basecharacter as bc
import battlemode as bm
import random
import battleround as br

possible_choice = {1: 'Undead', 2: 'Humans', 3: 'Beasts'}
#Choose Fraction
print("What fraction do you want to choose for battle?")
print("Please, put a number: 1 - Undead; 2 - Humans; 3 - Beasts")
answer = int(input())
chosen_fraction = possible_choice[answer]

#kinda menu
"""
print(f'So, you chose {chosen_fraction}, good choice!')
player_team = bm.comand_init(chosen_fraction)
print('Your team is:', end = ' ')
for unit in player_team: print(unit.name, end ='   ')
print('\n')
enemy_team = bm.random_enemy_team(chosen_fraction)
print('Enemy team is: ', end = ' ')
for unit in enemy_team: print(unit.name, end = '   ')
print('\n')
"""
print('write 4 names please:')
team = bm.CheckUnitsFraction(chosen_fraction)
player_team = bm.InitComand(team)
enemy_fraction = bm.EnemyFraction(chosen_fraction)
enemy_units = bm.EmenyUnitChoice(enemy_fraction)
print(f'Вражеская команда: {enemy_units}')
enemy_team = bm.InitComand(enemy_units)
br.Half_Auto_Battle(player_team, enemy_team)