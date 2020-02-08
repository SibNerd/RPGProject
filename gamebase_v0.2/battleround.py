'''
Решила вывести функцию боя в отдельный модуль. Возможно, в battlemode будут только функции
для обработки различной боевой логики, а здесь будет обработка самого боя.
'''
import battlemode as bm
import random

def Auto_Battle(player_team, enemy_team):
    """Function for automated battle. The only active ability is Attack.
    
    Arguments:
        player_team {list} -- list of player units
        enemy_team {list} -- list of enemy units
    """
    general_queue = bm.general_queue_logic(player_team, enemy_team)
    round_count = 1
    battle_loop = True
    while battle_loop:
        print(round_count, 'Round! Begin!')
        round_queue = big_battle_queue(general_queue)
        print(present_units(general_queue))
        print('Юниты в бою: ', units_in_battle(round_queue))
        for unit in round_queue:
            print(f"\nIt's {unit.name}'s turn to go. {unit.name} Has {unit.current_health} HP")
            defending_team = defence_turn(unit, player_team, enemy_team)
            enemy_unit = unit_turn(unit, defending_team)
            check_unit_from_team(enemy_unit, round_queue)
            battle_loop = check_for_battle_loop(player_team, enemy_team, round_queue)
            if not battle_loop: break
        print('End of the round ', round_count, '. \n')
        round_count +=1

def Half_Auto_Battle(player_team, enemy_team):
    """PvE battle. Units can use all their abilities.
    
    Arguments:
        player_team {list} -- list of player units
        enemy_team {list} -- list of enemy units
    """
    general_queue = bm.general_queue_logic(player_team, enemy_team)
    round_count = 1
    is_battle = True
    while is_battle:
        print(round_count, 'Раунд! Начали!')
        round_queue = big_battle_queue(general_queue)
        for unit in round_queue:
            print('\nЮниты в бою:', units_in_battle(round_queue))
            print(f"Cейчас ходит {unit.name}.")
            defending_team = defence_turn(unit, player_team, enemy_team)
            if unit in player_team:
                chosen_skill = PlayerSkillChoice(unit)
                skill_side_target = unit.Active_skills[chosen_skill]
                skill_side = ChosenSide(skill_side_target, player_team, enemy_team)
                enemy_target = ChosenSkillTarget(skill_side_target, skill_side)
                UseSkill(unit, chosen_skill, enemy_target)
            else: 
                enemy_target = unit_turn(unit, defending_team)
            check_unit_from_team(enemy_target, round_queue)
            is_battle = check_for_battle_loop(player_team, enemy_team, round_queue)
            if not is_battle: break
        print(f'Конец {round_count} раунда. \n')
        round_count +=1
            
           

def PlayerSkillChoice(unit):
    """Function for choosing an unit abitily.
    
    Arguments:
        unit {object} -- current unit.
    
    Returns:
        str -- name of chosen skill
    """
    possible_choice = []
    for skill in enumerate(unit.Active_skills):
        if skill not in unit.skills_on_CD:
            possible_choice.append(skill)
    print('Выберите номер способности, которую хотите использовать', possible_choice)
    answer = int(input())
    skill_name = possible_choice[answer][1]
    return skill_name

def ChosenSide(skill_target, player_team, enemy_team):
    """Function whis sets, whether ability's target player's or emeny's team.
    
    Arguments:
        skill_target {string} -- description of chosen abitily's target
        player_team {list} -- list of player's units
        enemy_team {list} -- list of enemy's units
    
    Returns:
        list -- chosen team
    """
    if 'friendly' in skill_target:
        chosen_team = player_team
    else:
        chosen_team = enemy_team
    return chosen_team

def ChosenSkillTarget(chosen_skill, team):
"""Function which sets, whether abitily's target will be single unit or whole team.

Arguments:
    chosen_skill {string} -- description of ability's target.
    team {list} -- target team, which will be target or in which single target will be selected.

Returns:
    object / list -- ability's target, object for single unit and list for whole team.
"""
    if 'team' in chosen_skill:
        chosen_target = ChooseTeam(team)
    elif 'target' in chosen_skill:
        chosen_target = ChooseTarget(team)
    return chosen_target

def ChooseTarget(team):
    """Function which sets single target.
    
    Arguments:
        team {list} -- list of possible targets
    
    Returns:
        object -- chosen target.
    """
    target_choice = []
    for pair in enumerate(team):
        if pair[1].alive:
            target_choice.append([pair[0], pair[1].name])
    print('Выберите номер противника, которого хотите сделать целью способности', target_choice)
    answer = int(input())
    for unit in team:
        if unit.name == target_choice[answer][1]:
            target = unit
    return target

def ChooseTeam(team):
    """Function which sets all alive units in team as a target.
    
    Arguments:
        team {list} -- list of all possible targets
    
    Returns:
        list -- list of all chosen targets
    """
    team_choice = []
    for unit in team:
        if unit.alive:
            team_choice.append(unit)
    return team_choice

def UseSkill(unit, skill_name, chosen_target):
    """Function which helps to apply unit's skill on it's target(s)
    
    Arguments:
        unit {object} -- current unit
        skill_name {string} -- mane of current skill
        chosen_target {object/list} -- skill's target(s), object for single target and list for multiple targets
    """
    skill = getattr(unit, skill_name)
    skill(chosen_target)

def big_battle_queue(original_queue):
    battle_queue = []
    for unit in original_queue:
        if (unit[0].alive and (unit[1]>0)):
            battle_queue.append(unit)
    round_queue = bm.Unique_initiative(battle_queue)
    round_units_queue = [i[0] for i in round_queue]
    return round_units_queue
    
def unit_turn(unit, enemy_team):
"""Simple AI turn prototype.
Uses basic Attack only.

Arguments:
    unit {object} -- current unit
    enemy_team {list} -- list of all possible targets

Returns:
    object -- enemy unit with dealt damage
"""
    current_choice = []
    for unit in enemy_team:
        if unit.alive:
            current_choice.append(unit)
    enemy_unit = random.choice(current_choice)
    unit.Attack(enemy_unit)
    enemy_unit.Is_alive()
    return enemy_unit

def defence_turn(unit, player_team, enemy_team):
    """Defending team checking
    
    Arguments:
        unit {object} -- current acting unit
        player_team {list} -- list of player's units
        enemy_team {list} -- list of emeny's units
    
    Returns:
        list -- defending team
    """
    if unit in player_team:
        defending_team = enemy_team
    elif unit in enemy_team:
        defending_team = player_team
    return defending_team

def check_for_battle_loop(player_team, enemy_team, big_queue):
    """Checks if both teams still have units. If not, sets loop = False
    
    Arguments:
        player_team {list} -- list of all current player's units
        enemy_team {list} -- list of all current emeny's units
        big_queue {list} -- list of all current units in battle
    
    Returns:
        bool -- True of both teams have at least one unit, False otherwise
    """
    if (set(player_team) >= set(big_queue)):
        return False
    elif (set(enemy_team) >= set(big_queue)):
        return False
    else: return True

def check_unit_from_team(target, round_queue):
    """Checks if unit os dead and if so, removes it from queue
    
    Arguments:
        target {object} -- target unit
        round_queue {list} -- list of all currnet acting units
    """
    if 'list' not in str(type(target)):
        print(f'У {target.name} осталось {target.current_health} здоровья.')
        target.Is_alive()
        if not target.alive:
            round_queue.remove(target)
            print(f'{target.name} умер.')
    else:
        for unit in target:
            print(f'У {unit.name} осталось {unit.current_health} здоровья.')
            unit.Is_alive
            if not unit.alive:
                round_queue.remove(unit)
                print(f'{unit.name} умер.')

# Данные две функции просто для наглядности выводят общий список и список очереди соответственно

def present_units(big_queue):
    all_units = []
    for unit in big_queue:
        all_units.append(unit[0].name)
    return all_units

def units_in_battle(round_q):
    rq = []
    for unit in round_q:
        rq.append([unit.name, unit.current_health])
    return(rq)
