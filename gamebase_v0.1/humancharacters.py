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
        super().__init__(morality=morality, rage=rage, effects={}, alive=alive)
        self.name = 'Домовой'
        self.max_health = 80
        self.current_health = 80
        self.strenght = 10
        self.initiative = 15


class Witcher(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, effects={}, alive=alive)
        self.name = 'Ведьмак'
        self.max_health = 130
        self.current_health = 130
        self.strenght = 15
        self.initiative = 8

class Protectress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, effects={}, alive=alive)
        self.name = 'Берегиня'
        self.max_health = 80
        self.current_health = 80
        self.strenght = 7
        self.initiative = 10

class HeroWarrior(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, effects={}, alive=alive)
        self.name = 'Богатырь'
        self.max_health = 180
        self.current_health = 180
        self.strenght = 12
        self.initiative = 5

class Druid(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self, morality=100, rage=0, alive=True):
        super().__init__(morality=morality, rage=rage, effects={}, alive=alive)
        self.name = 'Жрец'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 11
        self.initiative = 12
