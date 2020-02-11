import sqlite3

conn = sqlite3.connect('spells.db')

c = conn.cursor()

#c.execute('''CREATE TABLE spells
#							(name text, level integer, school text, castingtime text,range text,components text, duration text, discription text, higherlevels text, type text, dice text)''')

description = "A creature you touch regains a numer of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs"

higherlevel = "When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d8 for each slot level abovve 1st"

tablerow = (f'insert into spells values ("Cure Wounds",3,"evocation","1 action","Touch","V,S","Instantaneous","{description}","{higherlevel}","healing","1d8")')

c.execute(tablerow)
							
conn.commit()
conn.close()

# Spell Types -
# Healing
# Combat
# Utility
# Dice - Either how much damage or how much healing
