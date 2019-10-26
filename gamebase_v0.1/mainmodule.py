"""
MAIN GAME MODULE.
ALL THE GAME PROCESSES ARE PLACED HERE.
ALL THE FUNCTIONS CHECKIGS ARE PLASED HERE TOO (FOR NOW).
"""

import basecharacter as bc
import battlemode as bm
import undeadcharacters as udc
import humancharacters as huc
import beastcharacters as bec

possible_choice = {1: 'Undead', 2: 'Humans', 3: 'Beasts'}
#Choose Fraction
print("What fraction do you want to choose for battle?")
print("Please, put a number: 1 - Undead; 2 - Humans; 3 - Beasts")
answer = int(input())
chosen_fraction = possible_choice[answer]
#kinda menu
print('So, you chose {}, good choice!'.format(chosen_fraction))

#print('Your team:\n{},\n{}\n{}'.format)

"""
while priest.alive and skeleton.alive:
    skeleton_attack = skeleton.DoubleStrike()
    priest.health = bm.multiple_target_attack(skeleton_attack, priest.health)
    print ('Skeleton dealed {} damage to a priest, priest got {} health left.'.format(skeleton_attack, priest.health))
    priest.Health_check()
    if not priest.alive:
        print('priest died. RIP')
        break
    else:
        priest_attack = priest.Attack()
        skeleton.health = bm.single_target_attack(priest_attack, skeleton.health)
        print('Priest dealed {} gamage to a skeleton, skeleton got {} heslth left. \n'.format(priest_attack, skeleton.health))
        skeleton.Health_check()
        if not skeleton.alive:
            print('skeleton died. Finally.')
            break
        """

