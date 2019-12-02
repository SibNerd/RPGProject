"""
Module for all the Undead units.
"""

import basecharacter as bc
import random

class Imp(bc.BaseCharacter):
    """
    LOW DD UNIT.
    Future features: Can dodge SINGLE_TARGET attacks.
    Called 'Анчутка'
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, effects={}, alive=alive)
        self.name = 'Анчутка'
        self.max_health = 60
        self.current_health = 60
        self.strenght = 13
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
    '''
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, effects={}, alive=alive)
        self.name = 'Упырь'
        self.max_health = 80
        self.current_health = 80
        self.strenght = 15
        self.initiative = 11
       
    def Bite(self, enemy_unit):
        """
        Main ablity, Vampire not only gamages enemy, but also restores it's health.
        """
        biting_points = random.randint(1,20)
        total_bite = bc.check_parameter(self.strenght, biting_points)
        enemy_unit.current_health -= total_bite
        self.current_health += total_bite
        self.Check_current_health(self.current_health, self.max_health)


class Howleress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    Can heal other units in team.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, effects={}, alive=alive)
        self.name = 'Вытьянка'
        self.max_health = 70
        self.current_health = 70
        self.strenght = 15
        self.initiative = 10

    def RaiseTheDead(self, friendly_unit):
        """
        Resurrects one of the dead units and gives them 15 hp
        """
        friendly_unit.alive = True
        friendly_unit.health = 15
        #should i return anything here?        

    def Healing(self, friendly_unit):
        healing_points = random.randint(0,20)
        healing_done = bc.check_parameter(self.strenght, healing_points) # not final!
        pass

class Mara(bc.BaseCharacter):
    """
    CONTROL UNIT.
    Can control whole enemy team and and enemy units by one.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, effects={}, alive=alive)
        self.name = 'Мара'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 10
        self.initiative = 15
        
    def Horror(self, enemy_unit):
        """
        Controlling SINGLE_TARGET.
        """
        enemy_unit.initiative = 0
        enemy_unit.effects.update({'Horror': 2})

class Ghoul(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, effects={}, alive=alive)
        self.name = 'Вурдалак'
        self.health = 120
        self.strenght = 13
        self.initiative = 10
