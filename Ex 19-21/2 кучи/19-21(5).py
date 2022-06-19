def WIN1(x, s):
    # и для s, и для x в каждом вариенте по 2 варианта
    return (x + 1 + s >= 151) or (x + 4 + s >= 151)
def LOSS1(x, s):
    # Ваня выиграл посел любой игры Пети => Петя ходил из проигрышных, значит нужно найти проигр
    return (not(WIN1(x, s))) and WIN1(x+1, s) and WIN1(x, s+1) and WIN1(x+4, s) and WIN1(x, s+4)
def WIN2(x, s):
    return LOSS1(x+1, s) or LOSS1(x, s+1) or LOSS1(x+4, s) or LOSS1(x, s+4)

x = 11
for s in range(1, 137+1):
    # Ваня выиграл посел любой игры Пети => Петя ходил из проигрышных, значит нужно найти проигр
    #if LOSS1(x, s):
    #    print(s)
    #    break
    if WIN2(x, s):
        print(s)
        break
