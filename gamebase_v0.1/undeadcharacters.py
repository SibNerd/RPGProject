"""
Module for all the Undead units.
"""

import basecharacter as bc
import random

class SomeClass(bc.BaseCharacter):
    def __init__(self, morality=0, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
class Imp(bc.BaseCharacter):
    """
    LOW DD UNIT.
    Future features: Can dodge SINGLE_TARGET attacks.
    Called 'Анчутка'
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Анчутка'
        self.health = 70
        self.strenght = 23 #was 13
        self.initiative = 15
        self.agility = 10 #Used to check if unit dodged from damage
    
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
    Called 'Упырь'
    '''
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Упырь'
        self.health = 90
        self.strenght = 25 #was 15
        self.initiative = 11
       
    def Bite(self):
        biting_points = random.randint(1,20)

        pass

class Howleress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    Can heal other units in team.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Вытьянка'
        self.health = 80
        self.strenght = 25 #was 15
        self.initiative = 10

    def RaiseTheDead(self):
        pass

    
    def Healing(self):
        pass

class Mara(bc.BaseCharacter):
    """
    CONTROL UNIT.
    Can control whole enemy team and and enemy units by one.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Мара'
        self.health = 100
        self.strenght = 20 #was 10
        self.initiative = 15
        
    def Horror(self):
        """
        Controlling SINGLE_TARGET.
        """
        pass

class Ghoul(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Вурдалак'
        self.health = 140
        self.strenght = 23 #was 13
        self.initiative = 10
