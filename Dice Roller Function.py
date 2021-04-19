import secrets
def roll(userString, showMath = False):
    sum = 0
    newInput = []
    userStr = userString.split("+")
    for n in userStr:
        n = n.strip()
        if 'd' in n:
            n = n.split('d')
            for i in range(int(n[0])): newInput.append(secrets.randbelow(int(n[1]))+1)
        else:
            newInput.append(int(n))
    for i, item in enumerate(newInput):
        if showMath:
            if i: print(" + ", end = '')
            print(item, end = '')
        sum += item 
    if showMath: print()
    return sum