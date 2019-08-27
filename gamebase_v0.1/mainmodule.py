"""
MAIN GAME MODULE.
ALL THE GAME PROCESSES ARE PLACED HERE.
ALL THE FUNCTIONS CHECKIGS ARE PLASED HERE TOO (FOR NOW).
"""

import basecharacter as bc
import battlemode as bm
import undeadcharacters as udc

skeleton = udc.Imp()
priest = bc.BaseCharacter(strenght=10)

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