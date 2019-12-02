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
    def __init__(self, morality=100, rage=0, effects={}, alive=True):
        self.morality = morality
        self.rage = rage
        #self.defence = 0
        self.effects = {}
        self.alive = alive
        #self.action_points = 
        
    def Attack(self):
        """
        Basic Attack.
        Checks character's strenght only.
        """
        damage_points = random.randint(1,20) #perhaps should change to 30-40? or even 50 maybe
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
        defence_points = round((self.strenght/2) + (self.initiative/2))
        #defence_amount = (self.strenght + self.initiative)
        #total_defence = check_parameter(defence_amount, defence_points)
        return defence_points

    def Is_alive(self):
        '''
        Death of the character.
        Checks if charachers health points are above 0.
        If not, swithes SELF.ALIVE to FALSE.
        '''
        if self.health <= 0:
            self.alive = False
        
    def Check_current_health(self, current_health, max_health):
        if current_health > max_health:
            current_health = max_health