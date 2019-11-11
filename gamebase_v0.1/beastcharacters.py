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
        self.health = 90
        self.strenght = 22
        self.initiative = 13

class Werewolf(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Волколак'
        self.health = 80
        self.strenght = 22
        self.initiative = 12

class Swampress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Болотница'
        self.health = 110
        self.strenght = 22
        self.initiative = 10

class Werebear(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Берендей'
        self.health = 240
        self.strenght = 18
        self.initiative = 15

class Kikimora(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Кикимора'
        self.health = 120
        self.strenght = 25
        self.initiative = 7