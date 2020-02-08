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
    surpised = combat.surprise(locals()[suprises].abilitymod(locals()[suprises].ability['Dexterity'] + bonus),locals()[target].senses['Perception'])
else:
    surpised = None

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
            for item, _ in player.combat['Weapons'].items():
            		options.append(item)
        else:
            options = player.spellsknown['1']
        print('Select an option')
        for option in options:
            print(option)
        selection = None
        while selection not in options:
            selection = input('?')
        if action == 'A':
        		weapon = player.combat['Weapons'][selection]
        		if combat.attack(weapon['Bonus'], monster.combat['Armor Class']):
        				damage = roll(weapon['Damage'])
        				print(f'You have hit {monster.name} for {damage} points of damage.')
        		else:
        				print('Miss')
    else:
        print(f'You have been surprised as {monster.name} attacks you.')
        weapon = monster.combat['actions']['morning star']
        if combat.attack(weapon['attack'], player.combat['Armor Class']):
            damage = weapon['hit']
            print(f'You where hit by {monster.name} for {damage} points of damange.')
        else:
            print('Miss')
            
if suprises and not surpised:
    print(f'{locals()[target].name} is ready for combat and prepares to face {locals()[suprises].name}!')
