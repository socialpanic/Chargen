import random

GENDERS = ["Male", "Female"]
RACES = [
    "Human","Dwarf","Elf","Orc","Gnome","Tainted","Touched","Half-Orc","Half-Elf","Goblins","Drakkin","Dampyrs"
]

ALIGNMENT = [
   "Lawful",
   "Neurtal",
   "Chatoic"
]

SKILLS = [
    "Appraise – INT",
    "Craft – INT",
    "Diplomacy – CHA",
    "Handle Animal – CHA",
    "Jump - STR",
    "Labor - CON",
    "Knowledge - INT",
    "Perform - CHA",
    "Profession - WIS",
    "Ride - DEX",
    "Sense Motive - WIS",
    "Spot - WIS",
    "Survival - WIS",
    "Swim - STR",
    "Ceremony - WIS",
    "Heal - WIS",
    "Spellcraft - INT",
    "Endurance - CON",
    "Intimidate - CHA",
    "Leadership - CHA",
    "Balance - DEX",
    "Bluff - CHA",
    "Decipher Script - INT",
    "Disguise - CHA",
    "Escape Artist - DEX",
    "Forgery - INT",
    "Tumble - DEX"
]

VALUES = [
    "Community",
    "Adventure",
    "Charity",
    "Family",
    "Honesty",
    "Rule of Law",
    "Power",
    "Love",
    "Travel",
    "Reputation",
    "Knowledge",
    "Religion",
    "Humor",
    "Leadership",
    "Peace",
    "Vice",
    "Political Ideology",
    "Wealth",
    "Themselves",
    "Culture"
]

MONTHS = [
    "Justicar",
    "Fairah",
    "Marth",
    "Alfar",
    "Marpha",
    "J’khull",
    "Karn",
    "Vexx",
    "Sol",
    "Lyra",
    "Harth",
    "Deus",
]

VALUE1 = random.choice(VALUES)
VALUES.remove(VALUE1)
VALUE2 = random.choice(VALUES)
VALUES.remove(VALUE2)
VALUE3 = random.choice(VALUES)
VALUES.remove(VALUE3)

SCORN1 = random.choice(VALUES)
VALUES.remove(SCORN1)
SCORN2 = random.choice(VALUES)
VALUES.remove(SCORN2)
SCORN3 = random.choice(VALUES)
VALUES.remove(SCORN3)

DEADORALIVE = ["Dead", "Alive"]
PARENTALHERITAGE1 = random.choice(RACES)
PARENTALHERITAGE2 = random.choice(RACES)
RACE = random.choice (RACES)
GENDER = random.choice (GENDERS)
DOB_MONTH_DAY = str(random.choice (MONTHS)) +" "+str(random.randrange(1,30))
STR = random.randrange(3,19)
DEX = random.randrange(3,19)
INT = random.randrange(3,19)
WIS = random.randrange(3,19)
CON = random.randrange(3,19)
CHA = random.randrange(3,19)
HP = random.randrange(1,9)
COIN = random.randrange(3,181)

SIBLINGS = []
NO_OF_SIBS = random.randint(0,6)
SIBAGE = [
    "Younger",
    "Older"
]
SIBGENDER = [
    "Brother",
    "Sister"
]

for s in range(NO_OF_SIBS):
    young_or_old = random.choice(SIBAGE)
    brother_or_sister = random.choice(SIBGENDER)
    alive_or_dead = random.choice(DEADORALIVE)
    sib = young_or_old+" "+brother_or_sister+" "+alive_or_dead
    SIBLINGS.append(sib)

'''AGE = 0
if RACE == "Elf":
    AGE = random.randrange(114,134)
elif RACE == "Dwarf":
    AGE = random.randrange(43,58)
elif RACE == "Human":
    AGE = random.randrange(14,20)
elif RACE == "Orc":
    AGE = random.randrange(14,20)
elif RACE == "Gnome":
    AGE = random.randrange(44,64)
elif RACE == "Halfling":
    AGE = random.randrange(22,28)
elif RACE == "Half-Orc":
    AGE = random.randrange(14,20)
elif RACE == "Half-Elf":
    AGE = random.randrange(20,26)'''


print("==========================================================================================")
print("Race: "+RACE+"   ""Alignment: "+str(random.choice(ALIGNMENT))+"   "+ "Gender: "+GENDER+"   "+"DOB: "+str(DOB_MONTH_DAY))
print("HP: "+str(HP)+"     "+"COIN: "+str(COIN))
print("STR: "+str(STR)+"    "+"DEX: "+str(DEX)+"    "+"INT: "+str(INT)+"    "+"WIS: "+str(WIS)+"    "+"CON: "+str(CON)+"    "+"CHA: "+str(CHA))
print("Father: "+str(random.choice(DEADORALIVE)) + "    "+"Mother: "+str(random.choice(DEADORALIVE)))
print("Siblings: "+str(NO_OF_SIBS))
for s in SIBLINGS:
    print(s)
print("Values: "+VALUE1+", "+VALUE2+", "+VALUE3)
print("Scorns: "+SCORN1+", "+SCORN2+", "+SCORN3)
print("Skills: "+str(random.choice(SKILLS))+", "+str(random.choice(SKILLS))+", "+str(random.choice(SKILLS)))
print("==========================================================================================")

'''
import random

GENDERS = ["Male", "Female"]
RACES = [
    "Human",
    "Dwarf",
    "Elf",
    "Halfling",
    "Gnome",
    "Orc",
    "Drakkon",
    "Tainted",
    "Touched",
    "Half Orc",
    "Half Elf"
]
CLASSES = [
    "Bard",
    "Barbarian",
    "Fighter",
    "Cleric",
    "Thief",
    "Magic-User",
    "Druid",
    "Monk",
    "Sorcerer",
    "Paladin",
    "Ranger",
    "Illusionist"
    "Necromancer"
]

VALUES = [
    "Community", "Family", "Honesty", "Rule of Law", "Power", "Love", "Travel", "Reputation", "Knowledge", "Relgion", "Vice", "Humor", "Leadership", "Peace", "Political Idiology", "Wealth", "Own Ass", "Dignity", "Culture",
]

ALIGNMENTS = [
    "Lawful", "Neutal", "Chaotic"
]

HAIRCOLORS = [
    "Black",
    "Brown",
    "Red",
    "Blonde"
    "None"
]

PERSONAS = [
    'Friendly',
    'Grumpy',							
    'Ethical',				
    'Dishonest',
    'Polite',			
    'Brash',
    'Confident', 			
    'Arogant',         
    'Brave',					
    'Cowardly',
    'Diplomatic',			
    'Violent',
    'Attractive',		    
    'Ugly',
    'Patient',				
    'Reckless',
    'Charitable',			
    'Greedy',
    'Forgiving',				
    'Vengeful',        
    'Obedient',             
    'Rebellious',
    'Sociable',			
    'Reclusive'
]
    
HAIRLENGTHS = [
    "Long",
    "Short"
]

HAIRSTYLES = [
    "Wavey",
    "Straight",
    "Braided",
    "Poney Tail"
]

MONTHS = [
    "Justicar",
    "Fairah",
    "Marth",
    "Alfar",
    "Marpha",
    "J’khull",
    "Karn",
    "Vexx",
    "Sol",
    "Lyra",
    "Harth",
    "Deus",
]
DEADORALIVE = ["Dead", "Alive"]
RACE = random.choice (RACES)
HAIRLENGTH = random.choice (HAIRLENGTHS)
HAIRSTYLE = random.choice (HAIRSTYLES)
HAIRCOLOR = random.choice (HAIRCOLORS)
CLASS = random.choice (CLASSES)
ALIGNMENT = random.choice (ALIGNMENTS)
GENDER = random.choice (GENDERS)
DOB_MONTH_DAY = str(random.choice (MONTHS)) +" "+str(random.randrange(1,30))
STR = random.randrange(3,19)
STRMOD = 0
if STR == 3:
    STRMOD = -3
if STR == 4 or STR == 5:
    STRMOD = -2
if STR == 6 or STR == 7 or STR == 8:
    STRMOD = -1
if STR == 13 or STR == 14 or STR == 15:
    STRMOD = 1
if STR == 16 or STR == 17:
    STRMOD = 2
if STR == 18:
    STRMOD = 3

DEX = random.randrange(3,19)
DEXMOD = 0
if DEX == 3:
    DEXMOD = -3
if DEX == 4 or DEX == 5:
    DEXMOD = -2
if DEX == 6 or DEX == 7 or DEX == 8:
    DEXMOD = -1
if DEX == 13 or DEX == 14 or DEX == 15:
    DEXMOD = 1
if DEX == 16 or DEX == 17:
    DEXMOD = 2
if STR == 18:
    DEXMOD = 3

INT = random.randrange(3,19)
INTMOD = 0
if INT == 3:
    INTMOD = -3
if INT == 4 or INT == 5:
    INTMOD = -2
if INT == 6 or INT == 7 or INT == 8:
    INTMOD = -1
if INT == 13 or INT == 14 or INT == 15:
    INTMOD = 1
if INT == 16 or INT == 17:
    INTMOD = 2
if INT == 18:
    INTMOD = 3

WIS = random.randrange(3,19)
WISMOD = 0
if WIS == 3:
    WISMOD = -3
if WIS == 4 or WIS == 5:
    WISMOD = -2
if WIS == 6 or WIS == 7 or WIS == 8:
    WISMOD = -1
if WIS == 13 or WIS == 14 or WIS == 15:
    WISMOD = 1
if WIS == 16 or WIS == 17:
    WISMOD = 2
if WIS == 18:
    WISMOD = 3

CON = random.randrange(3,19)
CONMOD = 0
if CON == 3:
    CONMOD = -3
if CON == 4 or CON == 5:
    CONMOD = -2
if CON == 6 or CON == 7 or CON == 8:
    CONMOD = -1
if CON == 13 or CON == 14 or CON == 15:
    CONMOD = 1
if CON == 16 or CON == 17:
    CONMOD = 2
if CON == 18:
    CONMOD = 3

CHA = random.randrange(3,19)
CHAMOD = 0
if CHA == 3:
    CHAMOD = -3
if CHA == 4 or CHA == 5:
    CHAMOD = -2
if CHA == 6 or CHA == 7 or CHA == 8:
    CHAMOD = -1
if CHA == 13 or CHA == 14 or CHA == 15:
    CHAMOD = 1
if CHA == 16 or CHA == 17:
    CHAMOD = 2
if CHA == 18:
    CHAMOD = 3

COIN = random.randrange(3, 180)


if CLASS == "Fighter":
    HP = random.randrange(1,9)+CONMOD
if CLASS == "Cleric":
    HP = random.randrange(1,7)+CONMOD
if CLASS == "Magic-User":
    HP = random.randrange(1,5)+CONMOD
if CLASS == "Thief":
    HP = random.randrange(1,5)+CONMOD
if CLASS == "Paladin":
    HP = random.randrange(1,9)+CONMOD
if CLASS == "Ranger":
    HP = random.randrange(1,9)+CONMOD
if CLASS == "Sorcerer":
    HP = random.randrange(1,5)+CONMOD
if CLASS == "Monk":
    HP = random.randrange(1,7)+CONMOD
if CLASS == "Druid":
    HP = random.randrange(1,7)+CONMOD
if CLASS == "Bard":
    HP = random.randrange(1,5)+CONMOD
if CLASS == "Barbarian":
    HP = random.randrange(1,10)+CONMOD
if CLASS == "Illusionist":
    HP = random.randrange(1,5)+CONMOD

'''AGE = 0
if RACE == "Human":
    AGE = random.randrange(15,20)
if RACE == "Dwarf":
    AGE = random.randrange(40,60)
if RACE == "Elf":
    AGE = random.randrange(90,110)
if RACE == "Orc":
    AGE = random.randrange(13,19)
if RACE == "Halfling":
    AGE = random.randrange(20,30)
if RACE == "Gnome":
    AGE = random.randrange(40,60)
if RACE == "Half Elf":
    AGE = random.randrange(15,20)
if RACE == "Half Orc":
    AGE = random.randrange(15,20)'''

VALUE1 = random.choice(VALUES)
VALUES.remove(VALUE1)
VALUE2 = random.choice(VALUES)
VALUES.remove(VALUE2)
VALUE3 = random.choice(VALUES)
VALUES.remove(VALUE3)
SCORN1 = random.choice(VALUES)
VALUES.remove(SCORN1)
SCORN2 = random.choice(VALUES)
VALUES.remove(SCORN2)
SCORN3 = random.choice(VALUES)
VALUES.remove(SCORN3)

PERSONAINDEX = random.randrange(1,13)
PERSONA1 = PERSONAS[PERSONAINDEX]
del PERSONAS[PERSONAINDEX]
del PERSONAS[PERSONAINDEX+1]

PERSONAINDEX = random.randrange(1,13)
PERSONA2 = PERSONAS[PERSONAINDEX]
del PERSONAS[PERSONAINDEX]
del PERSONAS[PERSONAINDEX+1]

PERSONAINDEX = random.randrange(1,13)
PERSONA3 = PERSONAS[PERSONAINDEX]
del PERSONAS[PERSONAINDEX]
del PERSONAS[PERSONAINDEX+1]

DeathSave = 0
WandSave = 0
ParalysisSave = 0
Brath = 0
Spells = 0

MORALE = 9 + CONMOD

    "Bard",
    "Barbarian",
    "Fighter",
    "Cleric",
    "Thief",
    "Magic-User",
    "Druid",
    "Monk",
    "Sorcerer",
    "Paladin",
    "Ranger",
    "Illusionist"
    "Necromancer"


FighterClasses = [
    'Fighter',
    'Paladin',
    'Ranger',
    'Barbarian'
]

ThiefClasses = [
    'Thief',
    'Bard',
    'Monk',
    'Assassin'
]

MageClasses = [
    'Magic-user',
    'Sorcerer',
    'Necromancer',
    'Warlock'
]

ClericClasses = [
    'Ceric',
    'Druid',
    'Priest',
    'Inquisitor'
]
print("==========================================================================================")
print("Race: "+RACE+" Class: "+CLASS+  " Gender: "+GENDER+"  ALIGNMENT: "+ALIGNMENT+ "    MORALE: "+str(MORALE))
print("HP: "+str(HP)+"     "+"COIN: "+str(COIN)+ "    Hair: "+HAIRLENGTH+" "+HAIRCOLOR+" and "+HAIRSTYLE) 
print("STR: "+str(STR) +" " +str(STRMOD) + "              Death: ")   
print("DEX: "+str(DEX) +" " +str(DEXMOD) + "              Wands: ")
print("INT: "+str(INT) +" " +str(INTMOD) + "              Paralysis: ")
print("WIS: "+str(WIS) +" " +str(WISMOD) + "              Breath: ")
print("CON: "+str(CON) +" " +str(CONMOD) + "              Spels: ")
print("CHA: "+str(CHA) +" " +str(CHAMOD))
print("Mother: "+str(random.choice(DEADORALIVE)))
print("Father: "+str(random.choice(DEADORALIVE)))
print("Values: "+str(VALUE1)+", "+str(VALUE2)+", "+str(VALUE3))
print("Scorns: "+str(SCORN1)+", "+str(SCORN2)+", "+str(SCORN3))
print("Persona: "+str(PERSONA1)+", "+str(PERSONA2)+", "+str(PERSONA3))
print("==========================================================================================")

'''
