def WIN1(S):
    if (S + 4 >= 64) or (S*2 - 2 >= 64):
        return True
    return False

def LOSS1(S):
    if (not(WIN1(S))) and WIN1(S + 4) and WIN1(S*2 - 2):
        return True
    return False

def WIN2(S):
    if LOSS1(S + 4) or LOSS1(S*2 - 2):
        return True
    return False

def LOSS12(S):
    if WIN2(S + 4) and WIN1(S*2 - 2) or WIN2(S*2 - 2) and WIN1(S + 4):
        return True
    return False

a = []
b = []
c = []
for S in range(1, 63+1):
    if WIN1(S + 4) or WIN1(S*2 - 2):
        a.append(S)
    if WIN2(S):
        b.append(S)
    if LOSS12(S):
        c.append(S)
print('19:', min(a))
print('20:', min(b), max(b))
print('21:', min(c), c)