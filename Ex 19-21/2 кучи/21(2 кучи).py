def WIN1(x, S):
    if (x + S < 91) and ((x + 1 + S) >= 91 or (x*3 + S) >= 91 or (x + 3*S) >= 91):
        return True
    return False

def LOSS1(x, S):
    if (not(WIN1(x, S))) and WIN1(x, S + 1) and WIN1(x + 1, S) and WIN1(x*3, S) and WIN1(x, S*3):
        return True
    return False

def WIN2(x, S):
    if LOSS1(x, S + 1) or LOSS1(x + 1, S) or LOSS1(x*3, S) or LOSS1(x, S*3):
        return True
    return False

def LOSS12(x, S):
    if (WIN1(x, S + 1) or WIN2(x, S + 1)) and (WIN1(x + 1, S) or WIN2(x + 1, S)) and (WIN1(x*3, S) or WIN2(x*3, S)) and (WIN1(x, S*3) or WIN2(x, S*3)):
        return True
    return False

a = []
for S in range(1, 85):
    if LOSS12(14, S):
        a.append(S)
print(a)