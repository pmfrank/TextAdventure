from random import randint

def roll(dice):

    if '+' in dice:
        number, die, bonus = dice.replace('+','d').split('d')
        return randint(int(number),int(number)*int(die)) + int(bonus)
    number, die = dice.split('d')
    return randint(int(number),int(number)*int(die))
