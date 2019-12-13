'''
Решила вывести функцию боя в отдельный модуль. Возможно, в battlemode будут только функции
для обработки различной боевой логики, а здесь будет обработка самого боя.
'''
import battlemode as bm
import random

def Auto_Battle(player_team, enemy_team):
    general_queue = bm.general_queue_logic(player_team, enemy_team)
    round_count = 1
    battle_loop = True
    while battle_loop:
        print(round_count, 'Round! Begin!')
        #round_units_queue =  general_round_queue(player_team, enemy_team)
        #general_queue = bm.general_queue_logic(player_team, enemy_team)
        round_queue = big_battle_queue(general_queue)
        print(present_units(general_queue))
        print(units_in_battle(round_queue))
        for unit in round_queue:
            print(f"It's {unit.name}'s turn to go. {unit.name} Has {unit.current_health} HP")
            defending_team = defence_turn(unit, player_team, enemy_team)
            enemy_unit = unit_turn(unit, defending_team)
            check_unit_from_team(enemy_unit, round_queue)
            battle_loop = check_for_battle_loop(player_team, enemy_team, round_queue)
            if not battle_loop: break
        print('End of the round ', round_count, '. \n')
        round_count +=1

def Half_Auto_Battle(player_team, enemy_team):
    general_queue = bm.general_queue_logic(player_team, enemy_team)
    round_count = 1
    is_battle = True
    while is_battle:
        print(round_count, 'Round! Begin!')
        round_queue = big_battle_queue(general_queue)
        print(present_units(general_queue))
        print(units_in_battle(round_queue))
        for unit in round_queue:
            print(f"It's {unit.name}'s turn to go. {unit.name} Has {unit.current_health} HP")
            defending_team = defence_turn(unit, player_team, enemy_team)
            if unit in player_team:
                pass

def Player_choice(unit):
    possible_choice = []
    for skill in enumerate(unit.active_skills):
        if skill not in unit.skills_on_CD:
            possible_choice.append(skill)
    print('You can choose one skill to use, put a number please: ', possible_choice)
    chosen_skill = input()
    print(f'You chose {possible_choice[chosen_skill][1]}')

def big_battle_queue(original_queue):
    battle_queue = []
    for unit in original_queue:
        if (unit[0].alive and (unit[1]>0)):
            battle_queue.append(unit)
    round_queue = bm.Unique_initiative(battle_queue)
    round_units_queue = [i[0] for i in round_queue]
    return round_units_queue
    
def unit_turn(unit, enemy_team):
    """
    Автоход юнита. Прототип.
    """
    current_choice = []
    for unit in enemy_team:
        if unit.alive:
            current_choice.append(unit)
    enemy_unit = random.choice(current_choice)
    enemy_unit.current_health = bm.single_target_attack(unit.Attack(), enemy_unit.current_health)
    print(f'{enemy_unit.name} got {enemy_unit.current_health} HP left')
    enemy_unit.Is_alive()
    print(enemy_unit.alive)
    return enemy_unit
    
def defence_turn(unit, player_team, enemy_team):
    # Вывела проверку на принадлежность к команде в отдельную функцию, чтобы не было кучи вложенных циклов
    # Решила, что стоит возвращать список защищающейся команды
    if unit in player_team:
        defending_team = enemy_team
    elif unit in enemy_team:
        defending_team = player_team
    return defending_team

def check_for_battle_loop(player_team, enemy_team, big_queue): 
    if (set(player_team) >= set(big_queue)):
        return False
    elif (set(enemy_team) >= set(big_queue)):
        return False
    else: return True

def check_unit_from_team(unit, round_queue):
    # If unit is dead, removes it from queues and team
    if not unit.alive:
        round_queue.remove(unit)

# Данные две функции просто для наглядности выводят общий список и список очереди соответственно

def present_units(big_queue):
    all_units = []
    for unit in big_queue:
        all_units.append(unit[0].name)
    return all_units

def units_in_battle(round_q):
    rq = []
    for unit in round_q:
        rq.append(unit.name)
    return(rq)
