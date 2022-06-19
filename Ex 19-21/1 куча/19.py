# 19
def WIN1(S):
    # можно ли выиграть за один ход В?
    if S + 5 >= 78 or S*4 - 3 >= 78:
        return True
    else:
        return False

a = []

for S in range(1, 77+1):
    # позиции, которые делает П
    if WIN1(S + 5) or WIN1(S * 4 - 3):
        a.append(S)

print(min(a))