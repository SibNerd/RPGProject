"""
Basic functions for battles in game.
Contains different checks and queue logics by now.
"""

#import BaseCharacter
import random
import undeadcharacters
import humancharacters
import beastcharacters



# ВЫБОР ФРАКЦИЙ И СОЗДАНИЕ КОМАНД

possible_units = {
    'Анчутка': [undeadcharacters.Imp, 'Undead'], 
    'Упырь': [undeadcharacters.Vampire, 'Undead'],
    'Вытьянка': [undeadcharacters.Howleress, 'Undead'],
    'Мара': [undeadcharacters.Mara, 'Undead'],
    'Вурдалак': [undeadcharacters.Ghoul, 'Undead'],
    #'Костомаха': [undeadcharacters.Skeleton, 'Undead'],
    #'Жердяй': [undeadcharacters.Poleman, 'Undead'],
    #'Кадук': [undeadcharacters.Kaduk, 'Undead'],
    #'Бабай': [undeadcharacters.Babaiy, 'Undead'],
    #'Пепелюха': [undeadcharacters.Ashsoul, 'Undead'],

    'Домовой': [humancharacters.HouseSpirit, 'Humans'],
    'Ведьмак': [humancharacters.Witcher, 'Humans'],
    'Берегиня': [humancharacters.Protectress, 'Humans'],
    'Богатырь': [humancharacters.HeroWarrior, 'Humans'],
    'Жрец': [humancharacters.Druid, 'Humans'],
    #'Огневик': [humancharacters.Firesoul, 'Humans'],
    #'Витар': [humancharacters.SharpwindBird, 'Humans'],
    #'Русалка': [humancharacters.Mermaid, 'Humans'],
    #'Паляха': [humancharacters.FieldLady, 'Humans'],
    #'Чергавы': [humancharacters.Graveguard, 'Humans'],

    'Банник': [beastcharacters.Bather, 'Beasts'],
    'Волколак': [beastcharacters.Werewolf, 'Beasts'],
    'Болотница': [beastcharacters.Swampress, 'Beasts'],
    'Берендей': [beastcharacters.Werebear, 'Beasts'],
    'Кикимора': [beastcharacters.Kikimora, 'Beasts'],
    #'Жабалка': [beastcharacters.Toad, 'Beasts'],
    #'Аспид': [beastcharacters.Asp, 'Beasts'],
    #'Боровик': [beastcharacters.Boletus, 'Beasts'],
    #'Вужалка': [beastcharacters.TreeAspess, 'Beasts'],
    #'Леший': [beastcharacters.Forester, 'Beasts'],
}

def CheckUnitsFraction(fraction):
    """Пользовательское создание команды.
    Следит, что все юниты относятся к выбранной игроком фракции и являются уникальными.

    Args:
        fraction (string): выбранная игроком фракция

    Returns:
        list: список имен выбранных юнитов
    """
    group = []  
    while len(group) < 4:
        try:
            answer = str(input())
            unit = answer.capitalize()
            unit_fraction = possible_units.get(unit)[1]
            if (unit_fraction == fraction) and (unit not in group):
                group.append(unit)
                print(f'Ваша команда: {group}')
        except KeyboardInterrupt:
            print('Вы решили выйти из игры.')
            quit()
        except TypeError:
            print('Вы точно вводите имя юнита?')
            continue
    return group

def EmenyUnitChoice(fraction):
    choice = []
    group = []
    for unit in possible_units:
        if possible_units[unit][1] == fraction:
            choice.append(unit)
    while len(group) < 4:
        chosen_unit = random.choice(choice)
        group.append(chosen_unit)
        choice.remove(chosen_unit)
    return group

def EnemyFraction(chosen_fraction):
    possible_fractions = ['Undead', 'Humans', 'Beasts']
    possible_fractions.remove(chosen_fraction)
    enemy_fraction = random.choice(possible_fractions)
    return enemy_fraction

def InitComand(group):
    """Создает команду для боя.

    Arguments:
        group {set} -- список имен юнитов в команде

    Returns:
        list -- список объектов юнитов в команде
    """
    comand = []
    for unit in group:
        init_unit = possible_units.get(unit)[0]()
        comand.append(init_unit)
    return comand



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
