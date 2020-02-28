"""Module for all HUMAN units.
"""
import basecharacter as bc
import random

class HouseSpirit (bc.BaseCharacter):
    """
    LOW DD UNIT.
    Can't do shit actually.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Домовой'
        self.max_health = 80
        self.current_health = 80
        self.strenght = 12
        self.initiative = 19
        self.Active_skills = {'Attack': 'target',
                              'SuperDamage': 'target',}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def SuperDamage(self, target):
        cooldown = 3
        damage = int(self.strenght*1.5 + self.morality/100 + self.rage/10)
        target.current_health -= damage
        self.skills_on_CD.update({'SuperDamage': cooldown})
            
    # Конец активных способностей



class Witcher(bc.BaseCharacter):
    """
    HIGH DD UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Ведьмак'
        self.max_health = 130
        self.current_health = 130
        self.strenght = 15
        self.initiative = 13
        self.Active_skills = {'Attack': 'target',
                              'DamageAndStun': 'target',
                              'DamageBuff': 'self'}
        self.Passive_skills = {}
    
    # АКТИВНЫЕ СПОСОБНОСТИ

    def DamageAndStun(self, target):
        cooldown = 4
        damage = self.strenght
        stun_duration = 2
        target.current_health -= damage
        base_attr = target.initiative
        target.initiative = 0
        target.effects.update({'Stun': ['constant', base_attr, 'initiative', stun_duration]})
        self.skills_on_CD.update({'DamageAndStun': cooldown})
    
    def DamageBuff(self):
        cooldown = 4
        buff_amount = 3
        buff_duration = 2
        base_attr = self.strenght
        self.strenght += buff_amount
        self.effects.update({'DamageBuff': ['constant', base_attr, 'strenght', buff_duration]})
        self.skills_on_CD.update({'DamageBuff': cooldown})
            
    # Конец активных способностей


class Protectress(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Берегиня'
        self.max_health = 90
        self.current_health = 90
        self.strenght = 10
        self.initiative = 12
        self.Active_skills = {'Attack': 'target',
                              'TargetHealing': 'friendly target',
                              'RageDebuff': 'friendly team',}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def RageDebuff(self, target):
        cooldown = 2
        debuff_amount = 10
        for unit in target:
            unit.rage -= debuff_amount
        self.skills_on_CD.update({'RageDebuff': cooldown})

    def TargetHealing(self, target):
        cooldown = 3
        healing_amount = 15
        target.current_health += healing_amount
        target.Check_current_health()
        self.skills_on_CD.update({'TargetHealing': cooldown})
            
    # Конец активных способностей
    


class HeroWarrior(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Богатырь'
        self.max_health = 160
        self.current_health = 160
        self.strenght = 12
        self.initiative = 13
        self.Active_skills = {'Attack': 'target',
                              'TeamInitiativeBuff': 'friendly team',
                              'TeamMoralityBuff': 'friendly team',}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    def TeamInitiativeBuff(self, target):
        cooldown = 3
        buff_amount = 3
        buff_duration = 2
        for unit in target:
            base_atr = unit.initiative
            unit.initiative += buff_amount
            unit.effects.update({'Initiative Buff': ['constant', base_atr, 'initiative', buff_duration]})
        self.skills_on_CD.update({'TeamInitiativeBuff': cooldown}) 
    
    def TeamMoralityBuff(self, target):
        cooldown = 5
        buff_amount = 20
        buff_duration = 2
        for unit in target:
            base_atr = unit.morality
            unit.morality += buff_amount
            unit.effects.update({'Morality Buff', ['constant', base_atr, 'morality', buff_duration]})
        self.skills_on_CD.update({'TeamMoralityBuff': cooldown})
            
    # Конец активных способностей



class Druid(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Жрец'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 11
        self.initiative = 12
        self.Active_skills = {'Attack': 'target',
                              'TeamStrenghtDebuff': 'team',
                              'TargetInitiativeDebugg': 'target'}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ
    
    def TeamStrenghtDebuff(self, enenmies):
        COOLDOWN = 4
        debuff_amount = 4
        debuff_duration = 3
        for unit in enenmies:
            base_attr = unit.strenght
            unit.strenght -= debuff_amount
            unit.effects.update({'StrenghtDebuff': ['constant', base_attr, 'strenght', debuff_duration]})
        self.skills_on_CD.update({"TeamStrenghtDebuff": COOLDOWN})
    
    def TargetInitiativeDebuff(self, enemy):
        COOLDOWN = 3
        debuff_amount = 3
        debuff_duration = 2
        base_attr = enemy.initiative
        enemy.initiative -= debuff_amount
        enemy.effects.update({'InitiativeDebuff': ['constant', base_attr, 'initiative', debuff_duration]})
        self.skills_on_CD.update({'TargetInitiativeDebuff': COOLDOWN})
            
    # Конец активных способностей



class Firesoul(bc.BaseCharacter):
    def __init__(self):
        super().__init__()
        self.name = 'Огневик'
        self.max_health = 90
        self.current_health = 90
        self.strenght = 11
        self.initiative = 16
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей



class SharpwindBird(bc.BaseCharacter):
    def __init__(self):
        super().__init__()
        self.name = 'Витар'
        self.max_health = 120
        self.current_health = 120
        self.strenght = 15
        self.initiative = 12
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей


        
class Mermaid(bc.BaseCharacter):
    """
    SUPPORT UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Русалка'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 11
        self.initiative = 11
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей



class FieldLady(bc.BaseCharacter):
    """
    CONTROL UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Паляха'
        self.max_health = 110
        self.current_health = 110
        self.strenght = 13
        self.initiative = 11
        self.Active_skills = {}
        self.Passive_skills = {}

    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей


class Graveguard(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Чергавы'
        self.max_health = 170
        self.current_health = 170
        self.strenght = 14
        self.initiative = 11
        self.Active_skills = {}
        self.Passive_skills = {}
        
    # АКТИВНЫЕ СПОСОБНОСТИ

    # Конец активных способностей