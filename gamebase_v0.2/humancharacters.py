"""
Module for all the HUMAN units.
"""

import basecharacter as bc
import random

class HouseSpirit (bc.BaseCharacter):
    """
    LOW DD UNIT.
    Can't do shit actually.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Домовой'
        self.max_health = 80
        self.current_health = 80
        self.strenght = 12
        self.initiative = 15
        self.Active_skills = {'Атака': self.Attack,}
        self.Passive_skills = {}



class Witcher(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Ведьмак'
        self.max_health = 130
        self.current_health = 130
        self.strenght = 16
        self.initiative = 8
        self.Active_skills = {'Атака': self.Attack,}
        self.Passive_skills = {}



class Protectress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Берегиня'
        self.max_health = 90
        self.current_health = 90
        self.strenght = 10
        self.initiative = 10
        self.Active_skills = {'Атака': self.Attack,}
        self.Passive_skills = {}



class HeroWarrior(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Богатырь'
        self.max_health = 170
        self.current_health = 170
        self.strenght = 12
        self.initiative = 5
        self.Active_skills = {'Атака': self.Attack,}
        self.Passive_skills = {}



class Druid(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Жрец'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 11
        self.initiative = 12
        self.Active_skills = {'Атака': self.Attack,}
        self.Passive_skills = {}

    def Mass_Strenght_Debuff(self, enenmies):
        COOLDOWN = 4
        for unit in enenmies:
            unit.strenght -= 4
            unit.effects.update({'Stun': 3})
        self.skills_on_CD.update({"Mass_Strenght_Debuff": COOLDOWN})
    
    def Target_Initiative_Debuff(self, enemy):
        COOLDOWN = 3
        enemy.initiative -= 3
        enemy.effects.update({'Initiative debuff': 2})
        self.skills_on_CD.update({'Target Initiative Debuff': COOLDOWN})