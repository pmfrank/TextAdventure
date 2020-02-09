import re
from random import choice
from dice import roll

"""
1)  Determine suprise. The DM determies whether
    anyone involved in the combat encounter is
    surprised
2)  Establish positions. The DM decides where all the
    characters and monsters are located. Given th ad-
    venturer' marching orer or their stated position in
    the room or other location, the DM figures out where
    the adversaries are--how far away and in what
    direction
3)  Roll initiative.Everyone involved rolls initiative, de-
    termining the order of combatants' turns.
4)  Take turns. Each participant in the battle takes a
    turn in initiative order.
5)  Begin the next round. When evedryone involved in
    the combat has had a turn, the round ends. Repeat
    step 4 until the fighting stops.
"""

def position():
    """
    This function will only be used in the POC and will
    position will be handled differently as the game grows
    """

    range = ['melee','30','60','90','180']
    return choice(range)

def surprise(stealth, perception):
    """
    This function is used to determine surprise
    """

    check = roll(f'1d20+{str(stealth)}')
    if check > perception:
        return True
    return False

def initiative(dexterity):
    """
    This function is used to determine initiative
    """

    return roll(f'1d20+{str(dexterity)}')

def attack(modifier, ac):
    """
    This function is used to determine attack rolls
    """
    attackroll = roll(f'1d20+{str(modifier)}')
    if attackroll > ac:
        return True
    return False
    
def supriseattack(traits):
    
    """
    This function is used to determine if a monster has the surprise attack trait and how much extra damage they call do
    """
    
    reg = r'^\bSurprise\b'
    for trait in traits:
    	if re.match(reg, trait) is not None:
    		return trait.split('/')[1]
    return 0
