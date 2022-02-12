def WIN1(S):
    if S + 5 >= 78 or S*4 - 3 >= 78:
        return True
    return False


def LOSS1(S):
    #1) not(WIN1(S)) - позиция не должна быть выиграшной
    #2) S + 5 - выигр, потому что то, что из него можно получить истинно в WIN1
    #3) S*4 - 3 - выигр , потому что то, что из нее можно получить истинно в WIN1
    if (not(WIN1(S))) and WIN1(S + 5) and WIN1(S*4 - 3):
        return True # позиция выигрышная за 2 хода
    return False

def WIN2(S):
    # когда можем подложить свинью(чтобы выиграть за 2 хода)
    # LOSS1(S + 5) and LOSS1(S*4 - 3) - проверяем можем ли мы сделать проигр позицию
    # с самого начала S -> S(проигр)
    if LOSS1(S + 5) or LOSS1(S*4 - 3):
        return True
    return False

a = []
for S in range(1, 78):
    # if WIN1(S + 5) or WIN1(S*4 - 3):
    #     a.append(S)
    if WIN2(S):
        a.append(S)

# вывод максимального и минимального ответа
print(min(a), max(a))