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
        self.strenght = 10
        self.initiative = 15
        self.max_AP = self.Action_points()
        self.current_AP = self.Action_points()
        self.AP_restore = self.AP_restore_speed()


class Witcher(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Ведьмак'
        self.max_health = 130
        self.current_health = 130
        self.strenght = 15
        self.initiative = 8
        self.max_AP = self.Action_points()
        self.current_AP = self.Action_points()
        self.AP_restore = self.AP_restore_speed()

class Protectress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Берегиня'
        self.max_health = 80
        self.current_health = 80
        self.strenght = 7
        self.initiative = 10
        self.max_AP = self.Action_points()
        self.current_AP = self.Action_points()
        self.AP_restore = self.AP_restore_speed()
        self.Active_skills = {}
        self.Passive_skills = {}

class HeroWarrior(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Богатырь'
        self.max_health = 180
        self.current_health = 180
        self.strenght = 12
        self.initiative = 5
        self.max_AP = self.Action_points()
        self.current_AP = self.Action_points()
        self.AP_restore = self.AP_restore_speed()
        self.Active_skills = {}
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
        self.max_AP = self.Action_points()
        self.current_AP = self.Action_points()
        self.AP_restore = self.AP_restore_speed()
        self.Active_skills = {}
        self.Passive_skills = {}
