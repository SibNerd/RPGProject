import basecharacter as bc
import random

class HouseSpirit (bc.BaseCharacter):
    """
    LOW DD UNIT.
    Can't do shit actually.
    """
    def __init__(self, health=100, strenght=10, initiative=5, rage=0, defence=0, alive=True):
        super().__init__(health=health, strenght=strenght, initiative=initiative, rage=rage, defence=defence, alive=alive)

