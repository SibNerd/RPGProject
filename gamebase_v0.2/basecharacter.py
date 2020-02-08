"""Base characher module.

Has:
    Check_critical -- function for defoult Attack and other functions
"""
import random

# Зоны, в которых может выпасть значение кубика
CRITICAL_GOOD = range(1,5) 
GOOD = range(5, 9)
AVERAGE = range(9, 13)
BAD = range(14,17)
CRITICAL_BAD = range(17, 21)

def check_parameter (character_parameter, checking_points):
    """
    Checks if every ability was used successful.
    The smaller checking_points, the better.
    1-5 points mean critical hit, which doubles the result of the final points.
    """
    if checking_points <= character_parameter:
        if checking_points in CRITICAL_GOOD:
            resulting_points = character_parameter * 2
        else:
            resulting_points = checking_points
    else:
        resulting_points = 0
    return resulting_points

def Check_critical(character_parameter):
    """This function checks if Defoult Unit Parameter hit critical zone or not.
    
    Arguments:
        character_parameter {int} -- Defoult Character Number
        luck_factor {int} -- Random number used as a dice roll, then is checked on modificators.
    
    Modificators:
        CRITICAL_GOOD = doubles result
        GOOD = multiplies result by 1,5
        AVERAGE = does nothing
        BAD = divides result in half  
        CRITICAL_BAD = sets result as 0   
    Returns:
        result -- integer value, result of a dice roll
    """
    luck_factor = random.randint(0, 20)
    if luck_factor in CRITICAL_BAD:
        result = 0
    elif luck_factor in BAD:
        result = character_parameter / 2
    elif luck_factor in GOOD:
        result = character_parameter * 1,5
    elif luck_factor in CRITICAL_GOOD:
        result = character_parameter * 2
    else:
        result = character_parameter
    return result


class BaseCharacter():
    """Base module for every playable unit in game.
    Has several basic functions.

    Functions:
    Attack - basic attack
    Is_Alive - checks if unit is alive
    Check_currentHealth - checks unit's health in battle
    Check_Rage - checks unit's rage
    Check_Morality - ckecks unit's morality
    CooldownSkills - maintains skills on cooldown
    
    """
    def __init__(self):
        self.morality = 100
        self.rage = 0
        #self.defence = 0
        self.effects = {}
        self.skills_on_CD = {}
        self.alive = True
        
    def Attack(self, target):
        """Basic character Attack. Doesn't have a cooldown. Uses characters strenght and target's health.
        
        Arguments:
            target {object} -- target unit, who gets damage
        """
        damage_points = Check_critical(self.strenght)
        total_damage = int(damage_points * (self.morality/100) * (1-(self.rage/100)))
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
        #defence_amount = (self.strenght + self.initiative)
        #total_defence = check_parameter(defence_amount, defence_points)
        return defence_points

    def Is_alive(self):
        """Checks if unit is alive.
        If unit's current healt gets belov 0, unit dies.
        """
        if self.current_health <= 0:
            self.alive = False
        
    def Check_current_health(self):
        """Checks unit's current health.
        DOesn't let to have more than max_health.
        """
        if self.current_health > self.max_health:
            self.current_health = self.max_health
 
    def Check_Rage(self):
        """Checks unit's rage.
        Doesn't let rage be more than 100 or lwss than 0.
        Decreases Rage with every turn.
        """
        if self. rage > 100:
            self.rage = 100
        if self.rage > 0:
            self.rage -= 10
        elif self.rage <= 0:
            self.rage = 0

    def Check_Morality(self):
        """Check unit's morality.
        Doesn't let it drop less than 0.
        """
        if self.morality < 0:
            self.morality = 0

    def CooldownSkills(self):
        """Maintains skills' cooldown.
        If skill's CD sets below 0, deletes if from CD.
        """
        for skill in self.skills_on_CD:
            skill_CD = self.skills_on_CD.get(skill)
            skill_CD =- 1
            if skill_CD <= 0:
                del self.skills_on_CD[skill]