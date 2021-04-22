from Dice_Roller_Function import *
def charSheet(charName):
    with open(charName, 'r') as file:
        fileLines = file.readlines()

    for line in range(6,12):
        fileLines[line] = fileLines[line-6][0:3] + '_MOD ' + str((int(fileLines[line-6][4:-1])-10)//2) + '\n'

    with open(charName, 'w') as fileOut:
        fileOut.writelines(fileLines)

def abilityRoll(userString, charName):
    with open(charName, 'r') as file:
        fileLines = file.readlines()
    stats = ['STR','DEX','CON','INT','WIS','CHA']

    userString = userString.upper().strip()

    rollString = ''

    if userString[0:2] == 'A ': rollString += 'a '
    elif userString[0:2] == 'D ': rollString += 'd '
    rollString += '1d20+'

    try: assert userString[-3:] in stats
    except: return userString[-3:] + ' is not a valid stat.'

    rollString += str(fileLines[stats.index(userString[-3:])+6][8:-1])

    return roll(rollString, True)
    
