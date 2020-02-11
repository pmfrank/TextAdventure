from math import floor

class Entity():
	
    def __init__(self, **attributes):
        self.ability = {
            "Strength": int(attributes['strength']),
            "Dexterity": int(attributes['dexterity']),
            "Constitution": int(attributes['constitution']),
            "Intelligence": int(attributes['intelligence']),
            "Wisdom": int(attributes['wisdom']),
            "Charisma": int(attributes['charisma'])
        }
        self.combat = {
            "Armor Class": int(attributes['armorclass']),
            "Hit Points": int(attributes['hitpoints']),
            "Max HP": int(attributes['maxhitpoints']),
            "Hit Dice": str(attributes['hitdice']),
            "Speed": int(attributes['speed'])
        }
        self.languages = attributes['language']
        self.senses = {
            "Vision": str(),
            "Perception": int()
        }
        self.skills = list(attributes['skills'])

    def abilitymod(self, ability):
        return floor((ability -10) / 2)

class Player(Entity):

    def __init__(self, attributes, **playerinfo):
        super().__init__(**attributes)
        self.name = str(playerinfo['name'])
        self.playerclass = playerinfo['class']
        self.level = int(playerinfo['level'])
        self.race = str(playerinfo['race'])
        self.alignment = str(playerinfo['alignment'])
        self.experience = int(playerinfo['experience'])
        self.background = str(playerinfo['background'])
        self.combat['Weapons'] = dict(playerinfo['weapons'])
        self.features = list(playerinfo['features'])
        self.attacks = list(playerinfo['attacks'])
        self.spellslots = dict(playerinfo['spellslots'])
        self.currentslots = dict(playerinfo['currentslots'])
        self.spellsknown = dict(playerinfo['spellsknown'])
        self.gear = list(playerinfo['gear'])
        self.consumables = dict(playerinfo['consumables'])
        self.proficencybonus = int(playerinfo['proficiency'])
        self.senses['Perception'] = 10 + self.abilitymod(self.ability['Wisdom'])
        if 'Perception' in self.skills:
            self.senses['Perception'] = self.senses['Perception'] + self.proficencybonus
		
class Monster(Entity):
	
    def __init__(self, attributes, **monsterinfo):
        super().__init__(**attributes)
        self.name = str(monsterinfo['name'])
        self.damageimmunities = list(monsterinfo['damageimmunities'])
        self.conditionimmuities = list(monsterinfo['conditionimmunities'])
        self.challenge = str(monsterinfo['challengerating'])
        self.xp = int(monsterinfo['xp'])
        self.traits = list(monsterinfo['traits'])
        self.combat['actions'] = dict(monsterinfo['actions'])
        self.senses['Perception'] = int(monsterinfo['perception'])
