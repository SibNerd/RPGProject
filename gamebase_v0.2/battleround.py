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
        ApplyEffects(round_queue)
        for unit in round_queue:
            if unit.initiative >0:
                print('\nЮниты в бою:', units_in_battle(round_queue))
                print(f"Cейчас ходит {unit.name}, сила: {unit.strenght}.")
                if unit in player_team:
                    chosen_skill = PlayerSkillChoice(unit)
                    skill_side_target = unit.Active_skills[chosen_skill]
                    if skill_side_target == 'self':
                        skill_target = unit
                    else:
                        skill_side = PlayerChosenSide(skill_side_target, player_team, enemy_team)
                        skill_target = PlayerChosenSkillTarget(skill_side_target, skill_side)
                    UseSkill(unit, chosen_skill, skill_target)
                else:
                    chosen_skill = EnemySkillChoice(unit)
                    skill_side_target = unit.Active_skills[chosen_skill]
                    if skill_side_target == 'self':
                        skill_target = unit
                    else:
                        skill_side = EnemyChosenSide(skill_side_target, player_team, enemy_team)
                        skill_target = EnemyChosenSkillTarget(skill_side_target, skill_side)
                        print(f'{unit.name} использует {chosen_skill} на {skill_target}')
                    UseSkill(unit, chosen_skill, skill_target)
                check_unit_from_team(skill_target, round_queue)
                is_battle = check_for_battle_loop(player_team, enemy_team, round_queue)
                if not is_battle: break
            else: pass
        EffectsCooldown(round_queue)
        SkillsCooldown(round_queue)
        print(f'Конец {round_count} раунда. \n')
        round_count +=1
            
# Вспомогательные функции           

# Действие игрока

def PlayerSkillChoice(unit):
    """Function for choosing an unit abitily.    
    Arguments:
        unit {object} -- current unit.
    Returns:
        str -- name of chosen skill
    """
    possible_choice = []
    choice = []
    actives = unit.Active_skills.keys()
    on_cd = unit.skills_on_CD.keys()
    for skill in actives:
        if skill not in on_cd:
            possible_choice.append(skill)        
    for skill in enumerate(possible_choice):
            choice.append(skill)
    while True:
        try:
            print('Выберите номер способности, которую хотите использовать', choice)
            answer = int(input())
            if answer in range(len(choice)):
                skill_name = choice[answer][1]
                break
        except KeyboardInterrupt:
            print('You decided to quit the game.')
            quit()
        except:
            pass
        print('пожалуйста, введите корректное число.\n')
    return skill_name

def PlayerChosenSide(skill_target, player_team, enemy_team):
    """Function whis sets, whether ability's target player's or emeny's team.

    Returns:
        list -- chosen team
    """
    if 'friendly' in skill_target:
        chosen_team = player_team
    else:
        chosen_team = enemy_team
    return chosen_team

def PlayerChosenSkillTarget(chosen_skill, team):
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
        chosen_target = PlayerChooseTarget(team)
    return chosen_target

def PlayerChooseTarget(team):
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
    while True:
        try:
            print('Выберите номер юнита, которого хотите сделать целью способности', target_choice)
            answer = int(input())
            if answer in range(len(target_choice)):
                break
        except KeyboardInterrupt:
            print('You decided to quit the game.')
            quit()
        except:
            pass
        print('Пожалуйста, введите корректное число.\n')
    for unit in team:
        if unit.name == target_choice[answer][1]:
            target = unit
    return target

# Конец действий игрока

# Действие противника

def EnemySkillChoice(unit):
        possible_choice = []
        actives = unit.Active_skills.keys()
        on_cd = unit.skills_on_CD.keys()
        for skill in actives:
                if skill not in on_cd:
                        possible_choice.append(skill)
        chosen_skill = random.choice(possible_choice)
        return chosen_skill

def EnemyChosenSide(skill_target, player_team, enemy_team):
    if 'friendly' in skill_target:
        chosen_team = enemy_team
    else:
        chosen_team = player_team
    return chosen_team

def EnemyChosenSkillTarget(chosen_skill, team):
    if 'team' in chosen_skill:
        chosen_target = ChooseTeam(team)
    elif 'target' in chosen_skill:
        chosen_target = EnemyChooseTarget(team)
    return chosen_target

def EnemyChooseTarget(team):
        target_choice = []
        for unit in team:
                if unit.alive:
                        target_choice.append(unit)
        target = random.choice(target_choice)
        return target

# Конец действий противника

def ChooseTeam(team):
    """Function which sets all alive units in team as a target.

    Returns:
        list -- list of all chosen targets
    """
    team_choice = []
    for unit in team:
        if unit.alive:
            team_choice.append(unit)
    return team_choice

def UseSkill(unit, skill_name, chosen_target):
    """
    Function which helps to apply unit's skill on it's target(s)
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
    """Sets defending team.

    Returns:
        list -- defending team
    """
    if unit in player_team:
        defending_team = enemy_team
    elif unit in enemy_team:
        defending_team = player_team
    return defending_team

def check_for_battle_loop(player_team, enemy_team, big_queue):
    """Checks if both teams still have units.

    Returns:
        bool -- True if both teams have at least one unit, False otherwise
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
        target.Is_alive()
        if not target.alive:
            round_queue.remove(target)
            print(f'{target.name} умер.')
    else:
        for unit in target:
            # print(f'У {unit.name} {unit.current_health} здоровья.')
            unit.Is_alive()
            if not unit.alive:
                round_queue.remove(unit)
                print(f'{unit.name} умер.')

def SkillsCooldown(queue):
    for unit in queue:
        unit.CooldownSkills()

# Функции, управляющие эффектами юнитов

def ApplyEffects(queue):
    for unit in queue:
        if unit.effects:
            unit.ApplyActiveEffects()

def EffectsCooldown(queue):
    for unit in queue:
        if unit.effects:
            unit.CheckEffectCooldown()

# Данные две функции просто для наглядности выводят общий список и список очереди соответственно

def present_units(big_queue):
    all_units = []
    for unit in big_queue:
        all_units.append(unit[0].name)
    return all_units

def units_in_battle(round_q):
    rq = []
    for unit in round_q:
        if unit.alive and (unit.initiative > 0):
            rq.append([unit.name, unit.current_health])
    return(rq)
