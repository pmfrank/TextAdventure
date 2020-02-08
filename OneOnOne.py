from players import player
from monsters import monster
import combat
from dice import roll
from random import choice

print(f'You are {player.name}, the {player.race} {player.playerclass}. You have encounted a {monster.name}.')

suprises = choice(['player','monster',None])


if suprises:
    target = 'player' if suprises == 'monster' else 'monster'
    print(f'{locals()[suprises].name} has a chance to suprise {locals()[target].name}.')
    if suprises == 'monster':
        bonus = 0
    else:
        bonus = player.abilitymod(player.ability['Dexterity']) + player.proficencybonus if 'Stealth' in player.skills else player.abilitymod(player.ability['Dexterity'])
    surpised = combat.surprise(locals()[suprises].abilitymod(locals()[suprises].ability['Dexterity'] + bonus),10 + locals()[target].abilitymod(locals()[target].ability['Dexterity']))
else:
    surpised = None
suprises = 'player'
target = 'monster'
surpised = True
if surpised:
    print(f'{locals()[target].name} has been surprised by {locals()[suprises].name}.')
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
                for item, _ in weapon.items():
                    options.append(item)
        else:
            options = player.spellsknown['1']
        print('Select an option')
        for option in options:
            print(option)
        selection = None
        while selection not in options:
            selection = input('?')

if suprises and not surpised:
    print(f'{locals()[target].name} is ready for combat and prepares to face {locals()[suprises].name}!')
