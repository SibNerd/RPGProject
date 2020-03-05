"""
Содержит логику применения эффектов.

Есть два типа эффектов:
    * постоянные
    * прогрессивные

У постоянных эффектов передаются:
    * базовое значение
    * название измененного аттрибута
    * продолжительность

у прогрессивных эффектов передаются:
    * тип эффекта
    * модификатор
    * продолжительность

Прогрессивные эффекты накладываются в начале хода, продолжительность эффектов уменьшается в конце хода.
"""

class ConstantEffect():
    """
    Класс для постоянных эффектов.
    Принимает базовое значение, атрибут эффекта и продолжительность применения.
    """
    def __init__(self, effect):
        self.base = effect[1]
        self.attr = effect[2]
        self.duration = effect[3]

class ProgressiveEffect():
    """
    Класс для прогрессивных эффектов.
    Принимает тип эффекта, модификатор эффекта и продолжительность применения.
    """
    def __init__(self, effect):
        self.ftype = effect[1]
        self.amount = effect[2]
        self.duration = effect[3]
        
def GetEffectInfo(effect):
    """Делает из списка с описанием эффекта объект класса для удобства работы с его атрибутами
    
    Arguments:
        effect {list} -- список с атрибутами эффекта
    
    Returns:
        object -- объект класса ConstantEffect или ProgressiveEffect
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
