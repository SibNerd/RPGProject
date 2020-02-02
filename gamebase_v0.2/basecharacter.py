"""
Module for the basic character functions.
All team characters are based on BaseCharacter with modifications.
"""

import random

CRITICAL_GOOD = range(0,5) 
CRITICAL_BAD = range(15, 20)

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

def Check_critical(character_parameter):
    luck_factor = random.randint(0, 20)
    if luck_factor in CRITICAL_BAD:
        result = 0
    elif luck_factor in CRITICAL_GOOD:
        result = character_parameter * 2
    else:
        result = character_parameter
    return result


class BaseCharacter():
    def __init__(self):
        self.morality = 100
        self.rage = 0
        #self.defence = 0
        self.effects = {}
        self.skills_on_CD = {}
        self.alive = True
        
    def Attack(self, target):
        """
        Basic Attack.
        Checks character's strenght only.
        """
        damage_points = Check_critical(self.strenght)
        total_damage = int(damage_points * (self.morality/100) * (1-(self.rage/100)))
        target.current_health -= total_damage
    
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
        if self.current_health <= 0:
            self.alive = False
        
    def Check_current_health(self):
        if self.current_health > self.max_health:
            self.current_health = self.max_health
 
    def Check_Rage(self):
        if self. rage > 100:
            self.rage = 100
        if self.rage > 0:
            self.rage -= 10
        elif self.rage <= 0:
            self.rage = 0

    def Check_Morality(self):
        if self.morality < 0:
            self.morality = 0

    def CooldownSkills(self):
        for skill in self.skills_on_CD:
            skill_CD = self.skills_on_CD.get(skill)
            skill_CD =- 1
            if skill_CD <= 0:
                del self.skills_on_CD[skill]