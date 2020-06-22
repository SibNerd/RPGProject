"""
Module for all the Undead units.
"""

import basecharacter as bc
import random

class Imp(bc.BaseCharacter):
    """
    LOW DD UNIT.
    Future features: Can dodge SINGLE_TARGET attacks.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Анчутка'
        self.max_health = 60
        self.current_health = 60
        self.strenght = 14
        self.initiative = 20
        # self.agility = 10 # Used to check if unit dodged from damage
        self.Active_skills = {'Attack': 'target',
                              'DoubleStrike': 'target',}
        self.Passive_skills = {}
    
    # АКТИВНЫЕ СПОСОБНОСТИ

    def DoubleStrike(self, target):
        """
        Deals Damage to a target TWICE
        """
        cooldown = 2
        for i in range(2):
            dealt_damage = bc.CheckCritical((self.strenght)-2)
            print(f'{self.name} наносит {target.name} {dealt_damage} урона.')
            target.current_health -= dealt_damage
        self.skills_on_CD.update({"DoubleStrike": cooldown})

    # Конец активных способностей

    # ПАССИВНЫЕ СПОСОБНОСТИ
    # Конец пассивных способностей       



class Vampire(bc.BaseCharacter):
    '''
    HIGHT DD UNIT.
    '''
    def __init__(self):
        super().__init__()
        self.name = 'Упырь'
        self.max_health = 110
        self.current_health = 110
        self.strenght = 17
        self.initiative = 15
        self.Active_skills = {'Attack': 'target',
                              'Bite': 'target',}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def Bite(self, enemy_unit):
        """
        Main ablity, Vampire not only gamages enemy, but also restores it's health.
        Жажда крови
        """
        cooldown = 3
        biting_points = int(self.strenght + (1 + self.rage/100))
        total_bite = bc.CheckCritical(biting_points)
        enemy_unit.current_health -= total_bite
        self.current_health += total_bite
        self.Check_current_health()
        print(f'{self.name} наносит {enemy_unit.name} {total_bite} урона и восстанавливает себе здоровье на {total_bite}.')
        self.skills_on_CD.update({'Bite': cooldown})

    # Конец активных способностей



class Howleress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    Can heal other units in team.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Вытьянка'
        self.max_health = 70
        self.current_health = 70
        self.strenght = 13
        self.initiative = 14
        self.Active_skills ={ 'Attack': 'target',
                              'RaiseTheDead': 'friendly target', 
                              'Healing': 'friendly target',
                              'MassHealing': 'friendly team'}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def RaiseTheDead(self, friendly_unit):
        """
        Resurrects one of the dead units and gives them 35 hp
        Не Время умирать
        """
        COOLDOWN = 6
        friendly_unit.alive = True
        friendly_unit.current_health = 35
        print(f'{self.name} воскрешает {friendly_unit.name}, {friendly_unit} получает 35 ОЗ.')
        self.skills_on_CD.update({'RaiseTheDead': COOLDOWN})        

    def Healing(self, friendly_unit):
        """
        Вой по живым
        """
        COOLDOWN = 2
        healing_power = int((self.strenght + self.morality/100 + self.initiative/2))
        healing_done = bc.CheckCritical(healing_power)
        friendly_unit.current_health += healing_done
        friendly_unit.Check_current_health()
        print(f'{self.name} восстанавливает {friendly_unit.name} {healing_done} ОЗ.')
        self.skills_on_CD.update({"Healing": COOLDOWN})
    
    def MassHealing(self, team):
        cooldown = 4
        healing_power = int((self.strenght + self.morality/100 + self.initiative/2))
        healing_done = bc.CheckCritical(healing_power)
        for unit in team:
            unit.current_health += healing_done
            unit.Check_current_health()
        print(f'{self.name} восстанавливает здоровье команды на {healing_done} ОЗ.')
        self.skills_on_CD.update({'MassHealing': cooldown})

    # Конец активных способонстей



class Mara(bc.BaseCharacter):
    """
    CONTROL UNIT.
    Can control whole enemy team and and enemy units by one.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Мара'
        self.max_health = 110
        self.current_health = 110
        self.strenght = 17
        self.initiative = 15
        self.Active_skills = {'Attack': 'target',
                              'Horror': 'target',
                              'MassHorror': 'team',}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ 

    def Horror(self, unit):
        """
        Controlling SINGLE_TARGET.
        """
        COOLDOWN = 3
        stun_duration = 2
        base_attr = unit.initiative
        unit.initiative = 0
        unit.effects.update({'Stun': ['constant', base_attr, 'initiative', stun_duration]})
        print(f'{self.name} вводит в ужас {unit.name} на {stun_duration} хода.')
        self.skills_on_CD.update({'Horror': COOLDOWN})

    def MassHorror(self, team):
        COOLDOWN = 5
        stun_duration = 3
        for unit in team:
            base_attr = unit.initiative
            unit.initiative = 0
            unit.effects.update({'Stun': ['constant', base_attr, 'initiative', stun_duration]})
        print(f'{self.name} вводит в ужас команду противника на {stun_duration} хода')
        self.skills_on_CD.update({'MassHorror': COOLDOWN})

    # Конец активных способностей



class Ghoul(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Вурдалак'
        self.max_health = 140
        self.current_health = 140
        self.strenght = 14
        self.initiative = 16
        self.Active_skills = {'Attack': 'target',
                              'TeamStrenghtBuff': 'friendly team',}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def TeamStrenghtBuff(self, team):
        cooldown = 4
        duration = 2
        base_value = 5
        for unit in team:
            base_attr = unit.strenght
            unit.strenght += base_value
            unit.effects.update({'Strenght buff': ['constant', base_attr, 'strenght', duration]})
        print(f'{self.name} увеличивает урон команды на {base_value} единиц на {duration} хода.')
        self.skills_on_CD.update({'TeamStrenghtBuff': cooldown})
        
    # Конец активных способностей



class Skeleton(bc.BaseCharacter):
    """
    LOW DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Костомаха'
        self.max_health = 80
        self.current_health = 80
        self.strenght = 14
        self.initiative = 17
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей



class Poleman(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Жердяй'
        self.max_health = 110
        self.current_health = 110
        self.strenght = 16
        self.initiative = 13
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей



class Kaduk(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Кадук'
        self.max_health = 90
        self.current_health = 90
        self.strenght = 12
        self.initiative = 15
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей



class Babaiy(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Бабай'
        self.max_health = 110
        self.current_health = 110 
        self.strenght = 12
        self.initiative = 11
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей



class Ashsoul(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Пепелюха'
        self.max_health = 150
        self.current_health = 150
        self.strenght = 12
        self.initiative = 11
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей
