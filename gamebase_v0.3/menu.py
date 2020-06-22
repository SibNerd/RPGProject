"""
Модуль с главным меню игры.
Содержит функции для выбора фракции игрока, создания обеих команд, функцию самого главного меню
и функцию, обрабатывающую результат предыдущего боя.
"""

import battlemode as bm
import battleround as battle

def WonOrLose(winner):
    if winner:
        print('Вы выиграли! Что будете делать теперь?')
    else:
        print('Вы проиграли. Что будете делать теперь?')
"""
def AfterMatch(fraction, player_team, enemy_team):    
    print(""" """1 - Сыграть еще раз, ваша команда и команда противника будут прежние.
             2 - Сыграть еще раз, ваша команда останется прежней, но команда противника сменится.
             3 - Вернуться в меню.""" """)
    while True:
        try:
            answer = int(input())
            if answer == 1:
                player_team = 
                winner = battle.Auto_Battle(player_team, enemy_team)
                AfterMatch(fraction, player_team, enemy_team)
            elif answer == 2:
                enemy_units = CreateEnemyTeam(fraction)
                enemy_team = bm.InitComand(enemy_units)
                winner = battle.Auto_Battle(player_team, )
            elif answer == 3:
                MainMenu(fraction, player_team)
            else:
               print('Введите 1 или 2')
        except KeyboardInterrupt:
            quit()
        except:
            pass
"""



def MainMenu(fraction, team):
    if not fraction and not team:
        print('Привет! Давайте выберем вам фракцию и соберем команду, чтобы вы могли отправиться в бой!')
        fraction = ChooseFraction()
        player_team, enemy_team = CreateBothTeams(fraction)
        MainMenu(fraction, player_team)
    else:
        while True:
            try:
                print("""
                Выберите действие:
                1 - Пойти в бой.
                2 - Сменить команду.
                3 - Сменить фракцию.""")
                answer = int(input())
                if answer == 1:
                    enemy_units = CreateEnemyTeam(fraction)
                    player_team = bm.InitComand(team)
                    enemy_team = bm.InitComand(enemy_units)
                    winner = battle.Half_Auto_Battle(player_team, enemy_team)
                    WonOrLose(winner)
                elif answer == 2:
                    player_team, enemy_team = CreateBothTeams(fraction)
                    MainMenu(fraction, player_team)
                elif answer == 3:
                    fraction = ChooseFraction()
                    player_team, enemy_team = CreateBothTeams(fraction)
                    MainMenu(fraction, player_team)
                else:
                    print('Пожалуйста, введите правильное число')
            except KeyboardInterrupt:
                print('Вы решили выйти из игры. Вы уверены? При перезаходе вы начнете сначала. Y/N или Да/Нет')
                answer = str(input())
                if answer == 'Y' or 'y' or 'да' or 'Да' or "ДА":
                    quit()
                elif answer == 'N' or "n" or 'Нет' or 'нет' or 'НЕТ':
                    pass
                else:
                    print('Хмм... Примем это за нет.')
                    pass
            except ValueError:
                pass
            except TypeError:
                print('Вы уверены, что вводите число?')
                pass



# ----------------------Функции для выбора фракции и создания команд-------------------------

def CreateBothTeams(fraction):
    player_team = CreatePlayerTeam(fraction)
    enemy_team = CreateEnemyTeam(fraction)
    return [player_team, enemy_team]

def CreatePlayerTeam(fraction):
    unit_choice = []
    for name, info in bm.possible_units.items():
        if info[1] == fraction:
            unit_choice.append(name)
    print(f'Выберите 4 юнита из Следующих:{unit_choice}')
    team = bm.CheckUnitsFraction(fraction)
    return team

def CreateEnemyTeam(fraction):
    enemy_fraction = bm.EnemyFraction(fraction)
    enemy_units = bm.EmenyUnitChoice(enemy_fraction)
    print(f'Вражеская команда: {enemy_units}')
    return enemy_units

def ChooseFraction():
    possible_choice = {1: 'Undead', 2: 'Humans', 3: 'Beasts'}
    print("Какую фракцию вы хотите выбрать?")
    print("Пожалуйста, введите число: 1 - Нежить; 2 - Люди; 3 - Твари")
    while True:
        try:
            answer = int(input())
            if answer in range(1, 4):
                fraction = possible_choice[answer]
                return fraction
                break
            else:
                print('Пожалуйста, введите верное число')
        except KeyboardInterrupt:
            quit()
        except ValueError:
            print('Вы не ввели число.')
        except:
            print('Вы точно вводите число?')
            pass

