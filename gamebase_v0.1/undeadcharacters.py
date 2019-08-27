"""
ALl the UNDEAD and DARK characters are placed here. 
"""

import basecharacter as bc
import random

class Imp(bc.BaseCharacter):
    """
    LOW DD UNIT.
    Can dodge SINGLE_TARGET attacks.
    """
    def __init__(self, health=100, strenght=10, initiative=5, rage=0, alive=True):
        self.health = 80
        self.strenght = 15
        self.initiative = 15
        self.agility = 10
        self.rage = rage
        self.alive = alive
    
    def DoubleStrike(self):
        total_damage = list()
        for i in range(2):
            damage_points = random.randint(1,20)
            dealt_damage = bc.check_parameter((self.strenght-2), damage_points)
            total_damage.append(dealt_damage)
        return total_damage

class Vampire(bc.BaseCharacter):
    '''
    HIGHT DD UNIT.
    Has a lot of sthenght. Can heal himself by biting opponent SINGLE_TARGET units.
    '''
    def __init__(self, health=100, strenght=10, initiative=5, rage=0, alive=True):
        self.health = 100
        self.strenght = 15
        self.initiative = 10
        self.rage = rage
        self.alive = alive
        
    def Bite(self):
        biting_points = random.randint(1,20)

        pass

class Lich(bc.BaseCharacter):
    """
    HEALING UNIT.
    Can heal other units in team.
    """
    def __init__(self, health=100, strenght=10, initiative=5, rage=0, alive=True):
        self.health = 80
        self.strenght = 15
        self.initiative = 10
        self.rage = rage
        self.alive = alive

    def RaiseTheDead(self):
        pass

    
    def Healing(self):
        pass