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
        self.health = 90
        self.strenght = 20
        self.initiative = 15


class Witcher(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Ведьмак'
        self.health = 140
        self.strenght = 25
        self.initiative = 8

class Protectress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Берегиня'
        self.health = 100
        self.strenght = 17
        self.initiative = 10

class HeroWarrior(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Богатырь'
        self.health = 190
        self.strenght = 22
        self.initiative = 5

class Druid(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, alive=alive)
        self.name = 'Жрец'
        self.health = 110
        self.strenght = 21
        self.initiative = 12
