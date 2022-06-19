def WIN1(s):
    # Если позиция выигрышная, возвращает True
    return s + 3 >= 56 or 2*s >= 56

def LOSS1(s):
    # Проигрыш - как бы я не сходил, я проиграю, а соперник будет ходить из выигрышных
    return (not(WIN1(s))) and WIN1(s+3) and WIN1(2*s)

def WIN2(s):

    return LOSS1(s + 3) or LOSS1(2*s)


for s in range(1, 53):
    if WIN2(s):
        print(s)