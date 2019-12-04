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
        self.max_AP = self.Action_points()
        self.current_AP = self.Action_points()
        self.AP_restore = self.AP_restore_speed()
        self.Active_skills = {}
        self.Passive_skills = {}

class Werewolf(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Волколак'
        self.max_health = 70
        self.current_health = 70
        self.strenght = 12
        self.initiative = 12
        self.max_AP = self.Action_points()
        self.current_AP = self.Action_points()
        self.AP_restore = self.AP_restore_speed()
        self.Active_skills = {}
        self.Passive_skills = {}

class Swampress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Болотница'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 12
        self.initiative = 10
        self.max_AP = self.Action_points()
        self.current_AP = self.Action_points()
        self.AP_restore = self.AP_restore_speed()
        self.Active_skills = {}
        self.Passive_skills = {}

class Werebear(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Берендей'
        self.max_health = 220
        self.current_health = 220
        self.strenght = 8
        self.initiative = 15
        self.max_AP = self.Action_points()
        self.current_AP = self.Action_points()
        self.AP_restore = self.AP_restore_speed()
        self.Active_skills = {}
        self.Passive_skills = {}

class Kikimora(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Кикимора'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 15
        self.initiative = 7
        self.max_AP = self.Action_points()
        self.current_AP = self.Action_points()
        self.AP_restore = self.AP_restore_speed()
        self.Active_skills = {}
        self.Passive_skills = {}