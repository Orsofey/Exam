def WIN1(s):
    return s + 3 >= 56 or s * 2 >= 56
def LOSS1(s):
    return (not(WIN1(s))) and WIN1(s+3) and WIN1(s*2)
def WIN2(s):
    # ищем выигрышную позицию после WIN1
    return LOSS1(s+3) or LOSS1(s*2)

def LOSS12(s):
    return (WIN1(s+3) or WIN2(s+3)) and (WIN1(2*s) or WIN2(2*s))
for s in range(1, 53):
    if LOSS12(s):
        print(s)