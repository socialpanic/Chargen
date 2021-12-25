import random

GENDERS = ["Male", "Female"]
RACES = [
    "Human","Dwarf","Elf","Halfling","Gnome","Orc","Half Elf","Half Orc"
]
VALUES = [
    "Community",
    "Family",
    "Honesty",
    "Rule of Law",
    "Power",
    "Love",
    "Travel",
    "Reputation",
    "Knowledge",
    "Relgion / Dogma",
    "Pleasure",
    "Humor",
    "Leadership",
    "Peace",
    "Pleasure / Vice",
    "Political Idiology",
    "Wealth",
    "Own Ass",
    "Dignity",
    "Culture / Ethnicity",
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
GENDER = random.choice (GENDERS)
DOB_MONTH_DAY = str(random.choice (MONTHS)) +" "+str(random.randrange(1,30))
STR = random.randrange(3,18)
DEX = random.randrange(3,18)
INT = random.randrange(3,18)
WIS = random.randrange(3,18)
CON = random.randrange(3,18)
CHA = random.randrange(3,18)
HP = random.randrange(1,8)
COIN = random.randrange(6, 36)

AGE = 0
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
    AGE = random.randrange(15,20)


print("==========================================================================================")
print("Race: "+RACE+"   "+"Gender: "+GENDER+"   "+"DOB: "+str(DOB_MONTH_DAY) +", "+str(1986-AGE)+" A.F.    "+"Age: "+str(AGE))
print("HP: "+str(HP)+"     "+"COIN: "+str(COIN))
print("STR: "+str(STR))
print("DEX: "+str(DEX))
print("INT: "+str(INT))
print("WIS: "+str(WIS))
print("CON: "+str(CON))
print("CHA: "+str(CHA))
print("Mother: "+str(random.choice(DEADORALIVE)))
print("Father: "+str(random.choice(DEADORALIVE)))
print("Values: "+str(random.choice(VALUES))+", "+str(random.choice(VALUES))+", "+str(random.choice(VALUES)))
print("Scorns: "+str(random.choice(VALUES))+", "+str(random.choice(VALUES))+", "+str(random.choice(VALUES)))
print("==========================================================================================")