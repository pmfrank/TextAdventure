from classes import Monster

abilities = {
    'strength': 15,
    'dexterity': 14,
    'constitution': 13,
    'intelligence': 8,
    'wisdom': 11,
    'charisma': 9,
    'armorclass': 16,
    'hitpoints':27,
    'maxhitpoints': 27,
    'hitdice': '5d8+5',
    'speed': 30,
    'language': ['Common','Goblin'],
    'skills': ['Stealth','Survival']
}

monsterinfo = {
    'name': 'Bugbear',
    'damageimmunities': [],
    'conditionimmunities': [],
    'challengerating': '1',
    'xp': 200,
    'traits': ['Brute', 'Surprise Attack/2d6'],
    'actions': {'morning star':{'range':'melee','attack':4,'reach':5,'target':'one','hit':'2d8+2','type':'piercing'},
                'javelin':{'range':'ranged','attack':4,'reach':30,'target':'one','hit':'2d6+2','type':'piercing'}},
    'perception': 10
}

monster = Monster(abilities, **monsterinfo)
