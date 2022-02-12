def WIN1(S):
    if S + 5 >= 78 or S*4 - 3 >= 78:
        return True
    return False

def LOSS1(S):
    if (not(WIN1(S))) and WIN1(S + 5) and WIN1(S*4 - 3):
        return True
    return False

def WIN2(S):
    if LOSS1(S + 5) or LOSS1(S*4 - 3):
        return True
    return False

# проигр за 1 и 2 хода, чтобы Вероника могла ходить:
# 1) слева выиграть за 2 хода
# 2) справа выиграть за 1 ход
def LOSS12(S):
    if WIN2(S + 5) and WIN1(S*4 - 3) or WIN1(S + 5) and WIN2(S*4 - 3):
        return True
    return False

a = []
for S in range(1, 78):
    if LOSS12(S):
        a.append(S)
print(a)