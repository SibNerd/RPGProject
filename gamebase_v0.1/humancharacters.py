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
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Домовой'
        self.health = 100
        self.strenght = 10
        self.initiative = 15


class Witcher(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Ведьмак'
        self.health = 150
        self.strenght = 15
        self.initiative = 8

class Protectress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Берегиня'
        self.health = 110
        self.strenght = 7
        self.initiative = 10

class HeroWarrior(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Богатырь'
        self.health = 200
        self.strenght = 12
        self.initiative = 5

class Druid(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Жрец'
        self.health = 120
        self.strenght = 11
        self.initiative = 12
