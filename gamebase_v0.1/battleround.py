'''
Решила вывести функцию боя в отдельный модуль. Возможно, в battlemode будут только функции
для обработки различной боевой логики, а здесь будет обработка самого боя.
'''
import battlemode as bm
import random

def Auto_Battle(player_team, enemy_team):
    general_queue = bm.general_queue_logic(player_team, enemy_team)
    print(general_queue)
    round_count = 1
    battle_queue = []
    is_battle = True
    for unit in general_queue:
            if unit[0].alive:
                battle_queue.append(unit)
    round_queue = bm.Unique_initiative(battle_queue)
    round_units_queue = [i[0] for i in round_queue]
    while is_battle: #while both teams have units to fight
        print(round_count, 'Round! Begin!','\n')
        print(round_units_queue, '\n')
        for unit in round_units_queue:
            if unit in player_team:
                print(f'{unit.name} has to go.')
                en_unit = random.random.choice(enemy_team)
                print(f'{unit.name} chose to attack {en_unit.name}. {en_unit.name} got {en_unit.health} health')
                en_unit.health = bm.single_target_attack(unit.Attack(), en_unit.health)
                print(f'{unit.name} attacked {en_unit.name}, which got {en_unit.health} health left')
                en_unit.Is_alive()
                if not en_unit.alive:
                    round_units_queue.remove(en_unit)
                    enemy_team.remove(en_unit)
                    print(f'{en_unit.name} died')
                    if not enemy_team:
                        print('You won! Conrgatulations!')
                        is_battle = False
            elif unit in enemy_team:
                pl_unit = random.random.choice(player_team)
                print(f'{unit.name} chose to attack {pl_unit.name}. {pl_unit.name} got {pl_unit.health} health')
                pl_unit.health = bm.single_target_attack(unit.Attack(), pl_unit.health)
                print(f'{unit.name} attacked {pl_unit.name}, which got {pl_unit.health} hralth left')
                pl_unit.Is_alive()
                if not pl_unit.alive:
                    round_units_queue.remove(pl_unit)
                    player_team.remove(pl_unit)
                    print(f'{pl_unit.name} died')
                    if not player_team:
                        print('You lose. Try again.')
                        is_battle = False
        print('End of the round ', round_count, '. \n')
        round_count +=1

def unit_turn(unit):
    pass
"""
В чем идея:
взять повторяющийся код из верхней части и вывести его в отдельную функцию. В итоге в главной функции проверка идет на то,
к какой команде принадлежит юнит, и все.
В этой функции юнит будет ходить автоматически, возвращаться будет результат.
Главная функция будет обрабатывать результат.
"""