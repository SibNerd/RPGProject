"""Base characher module.

Has:
    Check_critical -- function for defoult Attack and other functions
"""
import random
import effects as EFFECTS

# Зоны, в которых может выпасть значение кубика, чем больше значение, тем _хуже_
CRITICAL_GOOD = range(1,5) 
GOOD = range(5, 9)
AVERAGE = range(9, 13)
BAD = range(13,17)
CRITICAL_BAD = range(17, 21)

def CheckCritical(character_parameter):
    """This function checks if Defoult Unit Parameter hit critical zone or not.
    
    Arguments:
        character_parameter {int} -- Defoult Character Number
        luck_factor {int} -- Random number used as a dice roll, then is checked on modificators.

    Returns:
        result -- integer value, result of a dice roll
    """
    luck_factor = random.randint(1, 20)
    if luck_factor in CRITICAL_BAD:
        result = 0
    elif luck_factor in BAD:
        result = character_parameter / 2
    elif luck_factor in GOOD:
        result = character_parameter * 1.5
    elif luck_factor in CRITICAL_GOOD:
        result = character_parameter * 2
    else:
        result = character_parameter
    return int(result)

# Возможно, добавлю функцию для проверки скилов, пусть пока будет здесь
# def UseCriticalSkill(parameter):
#    pass


class BaseCharacter():
    """
    Basic unit class. Maintains general attributes and functions.
    """
    def __init__(self):
        self.morality = 100
        self.rage = 0
        self.effects = {}
        self.skills_on_CD = {}
        self.alive = True
        
    def Attack(self, target):
        """Basic character Attack. Doesn't have a cooldown. Uses characters strenght, rage and morality and target's health.
        
        Arguments:
            target {object} -- target unit, who gets damage
        """
        damage_points = CheckCritical(self.strenght)
        modifiers = int((self.morality/100) * (1-(self.rage/100)))
        total_damage = damage_points * modifiers
        target.current_health -= total_damage
    
    def Defence(self):
        """
        Basic Defence.
        Perhaps will be used as TANK abitily only. Still thinking about it.
        """
        #defence_points = random.randint(0,20)
        #total_defence = check_parameter(self.strength, defence_points)
        # OR
        defence_points = round((self.strenght/2) + (self.initiative/2))
        return defence_points

    def Is_alive(self):
        """
        Checks if unit is alive. If unit's current healt gets belov 0, unit dies.
        """
        if self.current_health <= 0:
            self.alive = False
        
    def Check_current_health(self):
        """
        Checks unit's current health. Doesn't let to have more than max_health.
        """
        if self.current_health > self.max_health:
            self.current_health = self.max_health
 
    def Check_Rage(self):
        """
        Checks unit's rage.
        Doesn't let rage be more than 100 or less than 0.
        Decreases Rage with every turn.
        """
        if self. rage > 100:
            self.rage = 100
        if self.rage > 0:
            self.rage -= 10
        elif self.rage <= 0:
            self.rage = 0

    def Check_Morality(self):
        """
        Check unit's morality.
        Doesn't let it drop less than 0.
        """
        if self.morality < 0:
            self.morality = 0

    def CooldownSkills(self):
        """
        Maintains skills' cooldown.
        If skill's CD sets below 0, deletes if from CD.
        """
        for skill in tuple(self.skills_on_CD):
            self.skills_on_CD[skill] -= 1
            if self.skills_on_CD[skill] <= 0:
                del self.skills_on_CD[skill]
    
    def ApplyActiveEffects(self):
        """
        Applies all current effects on unit.
        Is used at the beginning of th e turn.
        """
        for effect in self.effects:
            current_effect = self.effects.get(effect)
            EFFECTS.ApplyEffect(current_effect)
            self.effects[effect][-1] -= 1
    

    def CheckEffectCooldown(self):
        """
        Maintains effects' cooldowns.
        Is used at the end of the turn.
        """
        for effect in tuple(self.effects):
            current_effect = self.effects.get(effect)
            if current_effect[0] == 'constant':
                if current_effect[-1] <= 0:
                    setattr(self, current_effect[2], current_effect[1])
                    del self.effects[effect]
            elif current_effect[0] == 'progressive':
                if current_effect[-1] <= 0:
                    del self.effects[effect]
        