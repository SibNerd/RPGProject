"""
Module for the basic character functions.
All team characters are based on BaseCharacter with modifications.
"""

import random

CRITICAL_GOOD = range(0,5) 
# Perhaps won't be used, but still better be named CRITICAL_BAD = range(15, 20)

def check_parameter (character_parameter, checking_points):
    """
    Checks if every ability was used successful.
    The smaller checking_points, the better.
    1-5 points mean critical hit, which doubles the result of the final points.
    """
    if checking_points <= character_parameter:
        if checking_points in CRITICAL_GOOD:
            resulting_points = character_parameter * 2
        else:
            resulting_points = checking_points
    else:
        resulting_points = 0
    return resulting_points


class BaseCharacter():
    def __init__(self, health=100, strenght=10, initiative=5, rage=0, defence=0, alive=True):
        self.health = 100
        self.strenght = 15
        self.initiative = 5
        self.rage = 0
        self.defence = 0
        self.alive = True

    def Attack(self):
        """
        Basic Attack.
        Checks character's strenght only.
        """
        damage_points = random.randint(1,20)
        total_damage = check_parameter(self.strenght, damage_points)
        return total_damage
    
    def Defence(self):
        """
        Basic Defence.
        Perhaps will be used as TANK abitily only. Still thinking about it.
        """
        #defence_points = random.randint(0,20)
        #total_defence = check_parameter(self.strength, defence_points)
        # OR
        defence_points = round(self.strenght / 2) + round(self.initiative / 2)
        defence_amount = (self.strenght + self.initiative)
        total_defence = check_parameter(defence_amount, defence_points)
        return total_defence

    def Health_check(self):
        '''
        Death of the character.
        Checks if charachers health points are above 0.
        If not, swithes SELF.ALIVE to FALSE.
        '''
        if self.health <= 0:
            self.alive = False
        
