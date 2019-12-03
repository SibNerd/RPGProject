'''
Решила вывести функцию боя в отдельный модуль. Возможно, в battlemode будут только функции
для обработки различной боевой логики, а здесь будет обработка самого боя.
'''
import battlemode as bm
import random

def Auto_Battle(player_team, enemy_team):
    round_count = 1
    while player_team and enemy_team:
        print(round_count, 'Round! Begin!','\n')
        round_units_queue =  general_round_queue(player_team, enemy_team)
        print(round_units_queue, '\n')
        for unit in round_units_queue:
            print(f"It's {unit.name}'s torn to go")
            defending_team = defence_turn(unit, player_team, enemy_team)
            enemy_unit = unit_turn(unit, defending_team)
            check_unit_from_team(enemy_unit, defending_team, round_units_queue)
            if not (player_team and enemy_team): break
        print('End of the round ', round_count, '. \n')
        round_count +=1

def general_round_queue(player_team, enemy_team):
    general_queue = bm.general_queue_logic(player_team, enemy_team)
    battle_queue = []
    for unit in general_queue:
            if unit[0].alive and (unit[0].initiative > 0):
                battle_queue.append(unit)
    round_queue = bm.Unique_initiative(battle_queue)
    round_units_queue = [i[0] for i in round_queue]
    return round_units_queue

def unit_turn(unit, enemy_team):
    """
    Автоход юнита. Прототип.
    """
    enemy_unit = random.choice(enemy_team)
    enemy_unit.current_health = bm.single_target_attack(unit.Attack(), enemy_unit.current_health)
    print(f'{enemy_unit.name} got {enemy_unit.current_health} HP left')
    enemy_unit.Is_alive()
    return enemy_unit
    
def defence_turn(unit, player_team, enemy_team):
    # Вывела проверку на принадлежность к команде в отдельную функцию, чтобы не было кучи вложенных циклов
    # Решила, что стоит возвращать список защищающейся команды
    if unit in player_team:
        defending_team = enemy_team
    elif unit in enemy_team:
        defending_team = player_team
    return defending_team

def check_unit_from_team(unit, team, round_units_queue):
    # If unit is dead, removes it from queues and team
    if not unit.alive:
        round_units_queue.remove(unit)
        team.remove(unit)

