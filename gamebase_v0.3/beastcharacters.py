"""
Module for all the BEAST units.
"""

import basecharacter as bc
import random

class Bather(bc.BaseCharacter):
    """
    LOW DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Банник'
        self.max_health = 90
        self.current_health = 90
        self.strenght = 12
        self.initiative = 15
        self.Active_skills = {'Attack': 'target',
                              'DamageAndStun': 'target'}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ
    
    def DamageAndStun(self, target):
        cooldown = 3
        stun_duration = 1
        damage = self.strenght/2
        target.current_health -= (damage)
        base_attr = target.initiative
        target.initiative = 0
        target.effects.update({'Stun': ['constant', base_attr, 'initiative', stun_duration]})
        print(f'{self.name} наносит {target.name} {damage} урона и обездвиживает на {stun_duration} хода.')
        self.skills_on_CD.update({'DamageAndStun': cooldown})

    # Конец активных способностей



class Werewolf(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Волколак'
        self.max_health = 130
        self.current_health = 130
        self.strenght = 14
        self.initiative = 12
        self.Active_skills = {'Attack': 'target',
                              'StrenghtBuff': 'self',
                              'MoralityBuff': 'friendly team'}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def StrenghtBuff(self):
        'rage of the beast'
        cooldown = 3
        value = 3
        buff_duration = 2
        base_attr = self.strenght
        self.strenght += value
        self.effects.update({'StrenghtBuff': ['constant', base_attr, 'strenght', buff_duration]})
        print(f'{self.name} увелеичивает свою силу на {value} единиц на {buff_duration} хода.')
        self.skills_on_CD.update({'StrenghtBuff': cooldown})
    
    def MoralityBuff(self, target):
        morality_amount = 15
        buff_duration = 2
        cooldown = 4
        for unit in target:
            base_attr = unit.morality
            unit.morality += morality_amount
            unit.effects.update({'MoralityBuff': ['constant', base_attr, 'morality', buff_duration]})
        print(f'{self.name} увеличивает мораль своей команды на {morality_amount} единиц на {buff_duration} хода.')
        self.skills_on_CD.update({'MoralityBuff': cooldown})

    # Конец активных способностей



class Swampress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Болотница'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 9
        self.initiative = 10
        self.Active_skills = {'Attack': 'target',
                              'MassHealing': 'friendly team',
                              'TargetStrenghtBuff': 'friendly target',}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def MassHealing(self, team):
        cooldown = 4
        healing_power = int((self.strenght + self.morality/100 + self.initiative/2))
        healing_done = bc.CheckCritical(healing_power)
        for unit in team:
            unit.current_health += healing_done
            unit.Check_current_health()
        self.skills_on_CD.update({'MassHealing': cooldown})
        print(f'{self.name} восстанавливает команде {healing_done} ОЗ.')

    def TargetStrenghtBuff(self, unit):
        cooldown = 3
        buff_amount = 2
        buff_duration = 2
        base_attr = unit.strenght
        unit.strenght += buff_amount
        unit.effects.update({'StrenghtBuff': ['constant', base_attr, 'strenght', buff_duration]})
        print(f'{self.name} увеличивает силу комнда на {buff_amount} единиц на {buff_duration} хода.')
        self.skills_on_CD.update({'TargetStrenghtBuff': cooldown})

    # Конец активных способностей


class Werebear(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Берендей'
        self.max_health = 190
        self.current_health = 190
        self.strenght = 8
        self.initiative = 6
        self.Active_skills = {'Attack': 'target',
                              'InitiativeBuff': 'friendly team',
                              'InitiativeBuffRageDebuff': 'friendly team',}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def InitiativeBuff(self, target):
        cooldown = 3
        buff_duration = 2
        buff_amount = 3
        for unit in target:
            base_attr = unit.initiative
            unit.initiative += buff_amount
            unit.effects.update({'InitiativeBuff': ['constant', base_attr, 'initiative', buff_duration]})
        print(f'{self.name} увеличивает инициативу команды на {buff_amount} единиц на {buff_duration} хода.')
        self.skills_on_CD.update({'InitiativeBuff': cooldown})

    def InitiativeBuffRageDebuff(self, target):
        cooldown = 4
        buff_amount = 2
        debuff_amount = 10
        buff_duration = 2
        for unit in target: 
            base_attr = unit.initiative
            unit.initiative += buff_amount
            unit.effects.update({'InitiativeBuff': ['constant', base_attr, 'initiative', buff_duration]})
            unit.rage -= debuff_amount
        print(f'{self.name} уввеличивает инициативу команды на {buff_amount} единиц на {buff_duration} хода и уменьшает ярость на {debuff_amount} единиц.')
        self.skills_on_CD.update({'InitiativeBuffRageDebuff': cooldown})
        
    # Конец активных способностей



class Kikimora(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Кикимора'
        self.max_health = 130
        self.current_health = 130
        self.strenght = 13
        self.initiative = 7
        self.Active_skills = {'Attack': 'target',
                              'Stun': 'target',
                              'InitiativeDebuff': 'team',
                              'RageBuff': 'target'}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def Stun(self, target):
        cooldown = 2
        stun_duration = 1
        base_attr = target.initiative
        target.initiative = 0
        target.effects.update({'Stun': ['constant', base_attr, 'initiative', stun_duration]})
        self.skills_on_CD.update({'Stun': cooldown})
        print(f'{self.name} обездвиживает {target.name} на {stun_duration} хода.')

    def InitiativeDebuff(self, target):
        cooldown = 4
        debuff_duration = 2
        debuff_amount = 3
        for unit in target:
            base_attr = unit.initiative
            unit.initiative -= debuff_amount
            unit.effects.update({'InitiativeDebuff': ['constant', base_attr, 'initiative', debuff_duration]})
        print(f'{self.name} уменьшает инициативу команды противника на {debuff_amount} единиц на {debuff_duration} хода.')
        self.skills_on_CD.update({'InitiativeDebuff': cooldown})

    def RageBuff(self, target):
        cooldown = 3
        buff_amount = 20
        buff_duration = 2
        target.rage += buff_amount
        target.effects.update({"RageBuff": ['progressive', 'buff', buff_amount, buff_duration]})
        print(f'{self.name} увеличивает ярость {target.name} на {buff_amount} единиц.')
        self.skills_on_CD.update({'RageBuff': cooldown})
    
    # Конец активных способностей



class Toad(bc.BaseCharacter):
    def __init__(self):
        super().__init__()
        self.name = 'Жабалка'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 11
        self.initiative = 15
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей



class Asp(bc.BaseCharacter):
    def __init__(self):
        super().__init__()
        self.name = 'Аспид'
        self.max_health = 130
        self.current_health = 130 
        self.strenght = 15
        self.initiative = 12
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей



class Boletus(bc.BaseCharacter):
    def __init__(self):
        super().__init__()
        self.name = 'Боровик'
        self.max_health = 180
        self.current_health = 180
        self.strenght = 13
        self.initiative = 12
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей



class TreeAspess(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Вужалка'
        self.max_health = 130
        self.current_health = 130
        self.strenght = 12
        self.initiative = 11
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей



class Forester(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Леший'
        self.max_health = 120
        self.current_health = 120
        self.strenght = 13
        self.initiative = 9
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей