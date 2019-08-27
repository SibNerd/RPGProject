#import BaseCharacter
#import random

"""
All the Battle functions and logic are placed here.

"""

def single_target_attack(attacking_character_damage, defending_character_health):
    """
    Standart attack.
    Used for abilities, where unit deals single gamage per action to a single target.
    """
    return defending_character_health - attacking_character_damage

def multiple_target_attack(attacking_character_damage=list, defending_character_health=int):
    """
    Used for abilities, where unit deals more than one damage per action to a single target.
    """
    for damage_dealt in attacking_character_damage:
        defending_character_health -= damage_dealt
    return defending_character_health

def AOE_target_attack(attacking_character_damage, defending_characters_health):
    resultiing_health = list()
    for defending_character in defending_characters_health:
        defending_character_health = defending_character - attacking_character_damage
        resultiing_health.append(defending_character_health)
    return resultiing_health