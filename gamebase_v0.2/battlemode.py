"""
Basic functions for battles in game.
Contains different checks and queue logics by now.
"""

#import BaseCharacter
import random
import undeadcharacters as uc
import humancharacters as hc
import beastcharacters as bc

# BASIC ATTACKING FUNCTIONS

def single_target_attack(attacking_character_damage, defending_character_health):
    """
    Standart attack.
    Used for abilities, where unit deals single gamage per action to a single target.
    """
    return defending_character_health - attacking_character_damage

def multiple_target_attack(attacking_character_damage, defending_character_health):
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

# End of Basic attacking funcktions



# FRACTION TEAMS INITIATION

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

# End of Fraction Teams Initiation



# TEAMS INITIATION

def comand_init(target_fraction):
    """Initiation of chosen fraction's command

    Arguments:
        target_fraction {string} -- chosen fraction

    Returns:
        list -- list of initialized units for battle
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
    """Initialises random enemy's team. Not the same as player's
    
    Arguments:
        chosen_fraction {string} -- player's chosen fraction
    
    Returns:
        list -- randomly set enemy's team
    """
    possible_fractions = ['Undead', 'Humans', 'Beasts']
    possible_fractions.remove(chosen_fraction)
    enemy_fraction = random.choice(possible_fractions)
    enemy_team = comand_init(enemy_fraction)
    return enemy_team

# end of player's & enemy's teams initiation



# QUEUE LOGIC OF THE BATTLE

def general_queue_logic(team_one_units, team_two_units):
    """Gets every unit in battle and sets them in GENERAL QUEUE by decreasing initiative

    Arguments:
        team_one_units {list} -- list of PLAYER units
        team_two_units {list} -- list of ENEMY units

    Returns:
        list -- GENERAL QUEUE with all units in battle
"""
    general_queue = []
    for unit in team_one_units:
        general_queue.append([unit, unit.initiative])
    for unit in team_two_units:
        general_queue.append([unit, unit.initiative])
    general_queue.sort(key=lambda x: x[1], reverse=True)
    return general_queue

def Unique_initiative(general_queue):
    """Checks unit's initiative and if finds the same, randomises them
    
    Returns:
        list -- randomised general queue
    """
    s_samples = sorted(general_queue, reverse=True, key=lambda x: x[1])
    for i in range(len(s_samples)-1):
        j = i+1
        if s_samples[i][1] == s_samples[j][1]:
            s_samples[i][1] = random.randint(1,s_samples[i][1])
            s_samples[j][1] = random.randint(1,s_samples[j][1])
    return sorted(s_samples, reverse=True, key=lambda x: x[1])
