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
        self.initiative = 13
        self.Active_skills = {'Attack': 'target',
                              'DamageAndStun': 'target'}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ
    
    def DamageAndStun(self, target):
        cooldown = 3
        stun_duration = 1
        damage = self.strenght/2
        target.current_health -= (damage)
        target.effects.update({'Stun': stun_duration})
        self.skills_on_CD.update({'DamageAndStun': cooldown})

    # Конец активных способностей



class Werewolf(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Волколак'
        self.max_health = 120
        self.current_health = 120
        self.strenght = 12
        self.initiative = 12
        self.Active_skills = {'Attack': 'target',
                              'DamageBuff': 'self',
                              'MoralityBuff': 'friendly team'}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def DamageBuff(self):
        'rage of the beast'
        cooldown = 2
        value = 3
        self.strenght += value
        self.effects.update({'Rage of the Beast': cooldown})
    
    def MoralityBuff(self, target):
        morality_amount = 15
        buff_duration
        cooldown = 4
        for unit in target:
            unit.morality += morality_amount
            unit.effects.update({'MoralityBuff': buff_duration})
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
        self.strenght = 10
        self.initiative = 10
        self.Active_skills = {'Attack': 'target',
                              'MassHealing': 'friendly team',
                              'TargetStrenghtBuff': 'friendly target',}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def MassHealing(self, team):
        cooldown = 4
        heal_value = 15
        for unit in team:
            unit.current_health += value
            unit.Check_current_health()
        self.skills_on_CD.update({'MassHealing': cooldown})

    def TargetStrenghtBuff(self, unit):
        cooldown = 3
        buff_amount = 2
        buff_duration = 2
        unit.strenght += buff_amount
        unit.effects.update({'StrenghtBuff', buff_duration})
        self.skills_on_CD.update({'TargetStrenghtBuff': cooldown})

    # Конец активных способностей


class Werebear(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Берендей'
        self.max_health = 200
        self.current_health = 200
        self.strenght = 10
        self.initiative = 15
        self.Active_skills = {'Attack': 'target',
                              'InitiativeBuff': 'friendly team',
                              'InitiativeBuffRageDebuff': 'team',}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def InitiativeBuff(self, target):
        cooldown = 3
        buff_duration = 2
        buff_amount = 3
        for unit in target:
            unit.initiative += buff_amount
            unit.effects.update({'InitiativeBuff': buff_duration})
        self.skills_on_CD.update({'InitiativeBuff': cooldown})

    def InitiativeBuffRageDebuff(self, target):
        cooldown = 4
        buff_amount = 2
        debuff_amount = 10
        buff_duration = 2
        for unit in target: 
            unit.initiative += buff_amount
            unit.effects.update({'InitiativeBuff': buff_duration})
            unit.rage -= debuff_amount
        self.skills_on_CD.update({'InitiativeBuffRageDebuff': cooldown})
        
        # Конец активных способностей



class Kikimora(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Кикимора'
        self.max_health = 110
        self.current_health = 110
        self.strenght = 15
        self.initiative = 7
        self.Active_skills = {'Attack': 'target',
                              'Stun': 'target',
                              'InitiativeDebuff': 'team',
                              'RageBuff': 'target'}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def Stun(self, target):
        cooldown = 3
        stun_duration = 2
        target.effects.update({'Stun': stun_duration})
        self.skills_on_CD.update({'Stun': cooldown})

    def InitiativeDebuff(self, target):
        cooldown = 5
        debuff_duration = 3
        debuff_amount = 3
        for unit in target:
            unit.initiative -= debuff_amount
            unit.initiative('InitiativeDebuff': debuff_duration)
        self.skills_on_CD.update({'InitiativeDebuff': cooldown})

    def RageBuff(self, target):
        cooldown = 4
        buff_amount = 20
        buff_duration = 2
        target.rage += buff_amount
        target.effects.update({"RageBuff": buff_duration})
        self.skills_on_CD.update({'RageBuff': cooldown})
    
    # Конец активных способностей