"""
Module for all the Undead units.
"""

import basecharacter as bc
import random

class Imp(bc.BaseCharacter):
    """
    LOW DD UNIT.
    Future features: Can dodge SINGLE_TARGET attacks.
    Called 'Анчутка'
    """
    def __init__(self):
        super().__init__()
        self.name = 'Анчутка'
        self.max_health = 60
        self.current_health = 60
        self.strenght = 13
        self.initiative = 15
        # self.agility = 10 # Used to check if unit dodged from damage
        self.Active_skills = {'Атака': self.Attack,
                              'Двойной удар': self.DoubleStrike,}
        self.Passive_skills = {}
    
    def DoubleStrike(self):
        """
        Deals Damage to a target TWICE
        """
        total_damage = list()
        for i in range(2):
            damage_points = random.randint(1,20)
            dealt_damage = bc.check_parameter((self.strenght-2), damage_points)
            total_damage.append(dealt_damage)
        return total_damage



class Vampire(bc.BaseCharacter):
    '''
    HIGHT DD UNIT.
    '''
    def __init__(self):
        super().__init__()
        self.name = 'Упырь'
        self.max_health = 80
        self.current_health = 80
        self.strenght = 17
        self.initiative = 11
        self.Active_skills = {'Атака': self.Attack,
                              'Жажда крови': self.Bite,}
        self.Passive_skills = {}
       
    def Bite(self, enemy_unit):
        """
        Main ablity, Vampire not only gamages enemy, but also restores it's health.
        """
        biting_points = random.randint(1,20)
        total_bite = bc.check_parameter(self.strenght, biting_points)
        enemy_unit.current_health -= total_bite
        self.current_health += total_bite
        self.Check_current_health(self.current_health, self.max_health)



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
        self.strenght = 11
        self.initiative = 12
        self.Active_skills = {'Атака': self.Attack,
                              'Не время умирать!': self.RaiseTheDead, 
                              'Вой по живым': self.Healing,
                              'Mass Healing': self.Mass_Healing}
        self.Passive_skills = {}

    def RaiseTheDead(self, friendly_unit):
        """
        Resurrects one of the dead units and gives them 35 hp
        """
        COOLDOWN = 6
        friendly_unit.alive = True
        friendly_unit.current_health = 35
        self.skills_on_CD.update({'Не время умирать!': COOLDOWN})        

    def Healing(self, friendly_unit):
        """
        Restores friendly target's HP.
        """
        COOLDOWN = 2
        healing_points = random.randint(0,20)
        healing_done = bc.check_parameter(self.strenght, healing_points) #mb change to CONST heal
        friendly_unit.current_health += healing_done
        friendly_unit.Check_current_health()
        self.skills_on_CD.update({"Вой по живым": COOLDOWN})
    
    def Mass_Healing(self, team):
        cooldown = 4
        healing_points = random.randint(0, 20)
        healing_done = bc.check_parameter(self.strenght, healing_points)
        for unit in team:
            unit.current_health += healing_done
            unit.Check_current_health()
        self.skills_on_CD.update({'Mass Healing': cooldown})



class Mara(bc.BaseCharacter):
    """
    CONTROL UNIT.
    Can control whole enemy team and and enemy units by one.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Мара'
        self.max_health = 100
        self.current_health = 100
        self.strenght = 11
        self.initiative = 14
        self.Active_skills = {'Атака': self.Attack,
                              'Horror': self.Horror,
                              'Mass Horor': self.Mass_Horror,}
        self.Passive_skills = {}
        
    def Horror(self, enemy_unit):
        """
        Controlling SINGLE_TARGET.
        """
        COOLDOWN = 3
        enemy_unit.initiative = 0
        enemy_unit.effects.update({'Stun': 3})
        self.skills_on_CD.update({'Horror': COOLDOWN})

    def Mass_Horror(self, team):
        COOLDOWN = 5
        for unit in team:
            unit.initiative = 0
            unit.effects.update({'Stun': 2})
        self.skills_on_CD.update({'Mass_Horror': COOLDOWN})



class Ghoul(bc.BaseCharacter):
    """
    TANK UNIT.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Вурдалак'
        self.max_health = 120
        self.current_health = 120
        self.strenght = 13
        self.initiative = 10
        self.Active_skills = {'Атака': self.Attack,
                              'Mass Strenght Buff': self.Mass_Strenght_Buff,}
        self.Passive_skills = {}

    def Mass_Strenght_Buff(self, team):
        cooldown = 4
        duration = 2
        base_value = 5
        for unit in team:
            unit.strenght += base_value
            unit.effects.update({'Strenght buff': duration})
        self.skills_on_CD.update({'Mass Strenght Buff': cooldown})