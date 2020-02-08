from players import player
from monsters import monster
import combat
from dice import roll
from random import choice

print(f'You are {player.name}, the {player.race} {player.playerclass}. You have encounted a {monster.name}.')

suprises = choice(['player','monster',None])


if suprises:
    target = 'player' if suprises == 'monster' else 'monster'
    print(f'{globals()[suprises].name} has a chance to suprise {globals()[target].name}.')
    if suprises == 'monster':
        bonus = 0
    else:
        bonus = player.abilitymod(player.ability['Dexterity']) + player.proficencybonus if 'Stealth' in player.skills else player.abilitymod(player.ability['Dexterity'])
    surpised = combat.surprise(globals()[suprises].abilitymod(globals()[suprises].ability['Dexterity'] + bonus),10 + globals()[target].abilitymod(globals()[target].ability['Dexterity']))
else:
    surpised = None
suprises = 'player'
target = 'monster'
surpised = True
if surpised:
    print(f'{globals()[target].name} has been surprised by {globals()[suprises].name}.')
    if suprises == 'player':
        print('With the element of suprise you get one free action. What will you do.')
        action = ''
        while action != 'A' and action != 'C':
            action = input('Action? (A)ttack (C)ast ')
            action = action[0].upper()
        options = list()
        if action == 'A':
            weapons = player.combat['Weapons']
            for weapon in weapons:
                for k,v in weapon.items():
                    options.append(k)
        else:
            options = player.spellsknown['1']
        print('Select an option')
        for option in options:
            print(option)
        selection = None
        while selection not in options:
            selection = input('?')

if suprises and not surpised:
    print(f'{globals()[target].name} is ready for combat and prepares to face {globals()[suprises].name}!')