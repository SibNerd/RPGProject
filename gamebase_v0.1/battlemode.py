#import BaseCharacter
import random
import undeadcharacters as uc
import humancharacters as hc
import beastcharacters as bc

"""
All the Battle functions and logic are placed here.
"""

#Basic attacking functions.

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
    """
    Used for abilities where unit deals single damage per action to more than one enemy.
    """
    resultiing_health = list()
    for defending_character in defending_characters_health:
        defending_character_health = defending_character - attacking_character_damage
        resultiing_health.append(defending_character_health)
    return resultiing_health

#end of Basic attacking funcktions


#FRACTION TEAMS INITIATION
def Undead_team_init():
    imp = uc.Imp()
    mara = uc.Mara()
    ghoul = uc.Ghoul()
    team_units = [imp, mara, ghoul]
    return team_units

def Humans_team_init():
    houser = hc.HouseSpirit()
    protectress = hc.Protectress()
    hero = hc.HeroWarrior()
    team_units = [houser, protectress, hero]
    return team_units

def Beasts_team_init():
    bather = bc.Bather()
    swampress = bc.Swampress()
    kikimora = bc.Kikimora()
    team_units = [bather, swampress, kikimora]
    return team_units

#end of Fraction Teams Initiation


#Player's and enemy's teams initiation
def comand_init(target_fraction):
    """
    Initiation of chosen fraction command.
    """
    #possible_fractions = (Undead, Humans, Beasts)
    if target_fraction == 'Undead':
        team = Undead_team_init()
    elif target_fraction == 'Humans':
        team = Humans_team_init()
    elif target_fraction == 'Beasts':
        team = Beasts_team_init()
    return team

def random_enemy_team(chosen_fraction):
    possible_fractions = ['Undead', 'Humans', 'Beasts']
    possible_fractions.remove(chosen_fraction)
    enemy_fraction = random.choice(possible_fractions)
    enemy_team = comand_init(enemy_fraction)
    return enemy_team


#end of player's & enemy's teams initiation

#Queue logic of the battle.
def round_queue_logic(team_one_units, team_two_units):
    """
    Gets list of all the present aka ALIVE units in current round and puts them in the order 
    of decreasing initiative points.
    """
    pass
