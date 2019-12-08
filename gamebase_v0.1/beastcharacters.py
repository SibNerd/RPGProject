"""
Module for all the BEAST units.
"""

import basecharacter as bc
import random

class Bather(bc.BaseCharacter):
    """
    LOW DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Банник'
        self.max_health = 90
        self.current_health = 90
        self.strenght = 12
        self.initiative = 13
        self.Active_skills = {'Атака': self.Attack,}
        self.Passive_skills = {}



class Werewolf(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Волколак'
        self.max_health = 120
        self.current_health = 120
        self.strenght = 12
        self.initiative = 12
        self.Active_skills = {'Атака': self.Attack,}
        self.Passive_skills = {}

    def Rage_Of_the_Beast(self):
        cooldown = 2
        value = 3
        self.strenght += value
        self.effects.update({'Rage of the Beast': cooldown})



class Swampress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Болотница'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 10
        self.initiative = 10
        self.Active_skills = {'Атака': self.Attack,}
        self.Passive_skills = {}

    def Masss_Healing(self, team):
        cooldown = 4
        value = 25
        for unit in team:
            unit.current_health += value
            unit.Check_current_health()
        self.skills_on_CD.update({'Mass Healing': cooldown})

    def Target_Strenght_Buff(self, unit):
        pass

class Werebear(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Берендей'
        self.max_health = 200
        self.current_health = 200
        self.strenght = 10
        self.initiative = 15
        self.Active_skills = {'Атака': self.Attack,}
        self.Passive_skills = {}



class Kikimora(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Кикимора'
        self.max_health = 110
        self.current_health = 110
        self.strenght = 15
        self.initiative = 7
        self.Active_skills = {'Атака': self.Attack,}
        self.Passive_skills = {}