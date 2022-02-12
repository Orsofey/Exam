def WIN1(S):
    if (S + 1 >= 101) or (S*4 >= 101):
        return True
    else:
        return False

def LOSS1(S):
    if (not(WIN1(S))) and WIN1(S + 1) and WIN1(S*4):
        return True
    return False

def WIN2(S):
    if LOSS1(S+1) or LOSS1(S*4):
        return True
    return False

def LOSS12(S):
    if (WIN2(S + 1) and WIN1(S*4)) or (WIN2(S*4) and WIN1(S + 1)):
        return True
    return False

List_19 = []
List_20 = []
List_21 = []

for S in range(1, 100+1):
    if WIN1(S + 1) or WIN1(S*4):
        List_19.append(S)
    if WIN2(S):
        List_20.append(S)
    if LOSS12(S):
        List_21.append(S)

print(min(List_19))
print(List_20[0])
print(min(List_21))