import secrets
def roll(userString, showMath = False):

    userString = userString.lower()

    # Advantage: None = 0 (Default), Advantage = 1, Disadvantage = -1
    advantage = 0
    sum = 0
    mathList = []


    # Checks for advantage or disadvantage 
    if userString[0:2] == 'a ':
        advantage = 1
        userString = userString[2:]
    elif userString[0:2] == 'd ':
        advantage = -1
        userString = userString[2:]


    userStr = userString.split("+")


    for n in userStr:
        n = n.strip()

        if 'd' in n:

            n = n.split('d')
            try: int(n[0])
            except ValueError: return n[0] + ' is not an integer.'

            try: int(n[1])
            except ValueError: return n[1] + ' is not an integer.'

            
            for i in range(int(n[0])): 
                if advantage == 1:
                    mathList.append(max(secrets.randbelow(int(n[1]))+1, secrets.randbelow(int(n[1]))+1))
                elif advantage == -1:
                    mathList.append(min(secrets.randbelow(int(n[1]))+1, secrets.randbelow(int(n[1]))+1))
                else:
                    mathList.append(secrets.randbelow(int(n[1]))+1)



        else:
            try: int(n)
            except ValueError: return n + ' is not an integer.'


            mathList.append(int(n))


    outputString = ''


    for i, item in enumerate(mathList):

        if showMath:
            if i: outputString += " + "
            outputString += str(item)

        sum += item 


    if showMath: outputString += ' = '
    outputString += str(sum)

    return outputString