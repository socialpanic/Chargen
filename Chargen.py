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