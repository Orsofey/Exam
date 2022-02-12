def WIN1(S):
    if S + 1 >= 91 or S + 4 >= 91 or S*5 >= 91:
        return True
    return False

def LOSS1(S):
    if (not(WIN1(S))) and WIN1(S + 1) and WIN1(S + 4) and WIN1(S*5):
        return True
    return False

def WIN2(S):
    if LOSS1(S + 1) or LOSS1(S + 4) or LOSS1(S*5):
        return True
    return False

def LOSS12(S):
    if (WIN2(S+1) and WIN1(S*5)) or (WIN2(S*5) and WIN1(S+1)) or (WIN2(S+4) and WIN1(S*5)) or (WIN2(S*5) and WIN1(S+4)) or (WIN2(S+4) and WIN1(S+1)) or (WIN2(S+1) and WIN1(S+4)):
        return True
    return False

List_19 = []
List_20 = []
List_21 = []
for S in range(1, 90+1):
    if WIN1(S + 1) or WIN1(S + 4) or WIN1(S*5):
        List_19.append(S)
    if WIN2(S):
        List_20.append(S)
    if LOSS12(S):
        List_21.append(S)
print(min(List_19))
print(min(List_20), max(List_20))
print(min(List_21))