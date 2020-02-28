"""
Содержит все эффекты и состояния, которые могут применятся к юнитам в бою

Есть два типа эффектов:
    * постоянные
    * прогрессивные

У постоянных эффектов передаются:
    * базовое значение
    * название измененного аттрибута
    * продолжительность

у прогрессивных эффектов передаются:
    * тип эффекта
    * базовое значение
    * модификатор
    * продолжительность

Прогрессивные эффекты накладываются в начале хода, продолжительность эффектов уменьшается в конце хода.
"""

from collections import namedtuple as ntp

class ConstantEffect():
    def __init__(self, effect):
        self.base = effect[1]
        self.attr = effect[2]
        self.duration = effect[3]

class ProgressiveEffect():
    def __init__(self, effect):
        self.ftype = effect[1]
        self.base = effect[2]
        self.amount = effect[3]
        self.duration = effect[4]
        
def GetEffectInfo(effect):
    """Делает из списка с описанием эффекта именованый список для удобства работы с его аттрибутами
    
    Arguments:
        effect {list} -- список с аттрибутами эффекта
    
    Returns:
        namedtuple -- именованый список
    """
    if effect[0] == 'constant':
        current_effect = ConstantEffect(effect)
    elif effect[0] == 'progressive':
        current_effect = ProgressiveEffect(effect)
    return current_effect

def ApplyEffect(effect):
    """Накладывает на юнита выбранный эффект.
    
    Arguments:
        effect {list} --   Список значений выбранного эффекта
    """
    if effect[0] == 'constant':
        current_effect = GetEffectInfo(effect)
    elif effect[0] == 'progressive':
        current_effect = GetEffectInfo(effect)
        ApplyProgressiveEffect(current_effect.ftype, current_effect.base, current_effect.amount)
   
def ApplyProgressiveEffect(ef_type, current_amount, mod_amount):
    possible_effects = {
    'buff': lambda: current_amount + mod_amount,
    'debuff': lambda: current_amount - mod_amount,
    }
    res_amount = possible_effects.get(ef_type, lambda: None)()
    return res_amount
