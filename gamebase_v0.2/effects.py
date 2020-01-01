"""
Содержит все эффекты и состояния, которые могут применятся к юнитам в бою
"""

# POSITIVE EFFECTS

def StrenghtBuff(unit):
    pass

def InitiativeBuff(unit):
    pass



# END OF POSITIVE



# NEGATIVE EFFECTS

def StrenghtDebuff(unit):
    pass

def InitiativeDebuff(unit):
    pass

def Stun(unit):
    '''
    Sets Initiative = 0
    '''
    unit.Initiative = 0

def Bleeding(unit):
    '''
    Deals damage every turn.
    '''
    pass

# END OF NEGATIVE EFFECTS



def ApplyEffects(unit):
    for effect in unit.effects:
        if effect == 'stun':
            Stun(unit)
        if effect == 'Bleeding':
            Bleeding(unit)
            