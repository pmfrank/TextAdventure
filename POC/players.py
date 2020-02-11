from classes import Player

abilities = {
    'strength': 16,
    'dexterity': 14,
    'constitution': 14,
    'intelligence': 10,
    'wisdom': 12,
    'charisma': 10,
    'armorclass': 16,
    'hitpoints':28,
    'maxhitpoints': 28,
    'hitdice': '3d10',
    'speed': 30,
    'language': ['Common','Orc','Deep Speech','Elvish'],
    'skills': ['Animal Handling','Athletics','Insight','Intimidation','Perception','Survival']
}

playerinfo = {
    'name': 'Grog',
    'class': 'Ranger',
    'level': 3,
    'race': 'Half-Orc',
    'alignment': 'Neutral Good',
    'experience': 900,
    'background': 'Outlander',
    'weapons': {'Longbow': {'Bonus': 6, 'Damage': '1d8+2', 'Type': 'Piercing'},
                'Shortsword': {'Bonus': 5, 'Damage': '1d6+3', 'Type': 'Piercing'}},
    'features': ('Favored Enemy (Monstrosities)','Natural Explorer (Forest)', 'Fighting Style (Archery)', 'Spellcasting', 'Prieval Awareness',
                'Relentless Endurance', 'Savage Attacks'),
    'attacks': ['Colossus Slayer'],
    'spellslots': {'1': 3},
    'currentslots': {'1': 3},
    'spellsknown': {'1':['Cure Wounds', 'hunter\'s mark', 'longstride']},
    'gear':['Scale Mail','Shortsword','Longbow','Backpack','Traveler\'s Clothes','Hunting Trap','Mess Kit', 'Hempen Rope (50ft)',
            'Tinderbox','Waterskin','Staff'],
    'consumables': {'Arrows': 20, 'Torch': 10,'Rations - 1 day': 10},
    'proficiency': 2
}

player = Player(abilities, **playerinfo)
