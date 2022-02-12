def WIN1(x, S):
    if (x + S < 44 ) and ((x + S + 1) >= 44 or (x + 2*S) >= 44 or (x*2 + S) >= 44):
        return True
    return False

def LOSS1(x, S):
    if (not(WIN1(x, S))) and WIN1(x, S + 1) and WIN1(x + 1, S) and WIN1(x*2, S) and WIN1(x, S*2):
        return True
    return False

def WIN2(x, S):
    if LOSS1(x, S + 1) or LOSS1(x + 1, S) or LOSS1(x, S*2) or LOSS1(x*2, S):
        return True
    return False

def LOSS12(x, S):
    if (WIN2(x + 1, S) or WIN1(x, S + 1)) and (WIN2(x*2, S) or WIN1(x, S*2)) and (WIN1(x + 1, S) or WIN2(x, S + 1)) and (WIN1(x*2, S) or WIN2(x, S*2)):
        return True
    return False

List_19 = []
List_20 = []
List_21 = []

for S in range(1, 39+1):
    if WIN1(5, S):
        List_19.append(S)
    if WIN2(5, S):
        List_20.append(S)
    if LOSS12(5, S):
        List_21.append(S)

print(min(List_19))
print(max(List_20))
print(min(List_21))