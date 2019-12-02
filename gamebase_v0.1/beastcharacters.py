"""
Module for all the BEAST units.
"""

import basecharacter as bc
import random

class Bather(bc.BaseCharacter):
    """
    LOW DD UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Банник'
        self.max_health = 90
        self.current_health = 90
        self.strenght = 12
        self.initiative = 13

class Werewolf(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Волколак'
        self.max_health = 70
        self.current_health = 70
        self.strenght = 12
        self.initiative = 12

class Swampress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Болотница'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 12
        self.initiative = 10

class Werebear(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Берендей'
        self.max_health = 220
        self.current_health = 220
        self.strenght = 8
        self.initiative = 15

class Kikimora(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Кикимора'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 15
        self.initiative = 7