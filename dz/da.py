# -1 /2
def WIN1(x, s):
    if x -1 + s <= 40 or x/2+ s <= 40 or x + s -1 <= 40 or x + s/2 <= 40:
        return True
    else:
        return False
def LOSS1(x, s):
    if (not(WIN1(x, s))) and WIN1(x-1, s) and WIN1(x/2, s) and WIN1(x, s -1) and WIN1(x, s/2):
        return True
    else:
        return False

def WIN2(x, s):
    if LOSS1(x+3, s) or LOSS1(x/2, s) or LOSS1(x, s-1) or LOSS1(x, s/2):
        return True
    else:
        return False

def LOSS12(x, s):
    if (WIN1(x, s-1) or WIN2(x, s-1)) and (WIN1(x/2, s) or WIN2(x/2, s)) and (WIN1(x, s/2) or WIN2(x, s/2)) and (WIN1(x-1, s) or WIN2(x-1, s)):
        return True
    else:
        return False
x = 6
x_19 = []
x_20 = []
x_21 = []
for s in range(11, 1000):
    if WIN1(x, s):
        x_19.append(s)
    if WIN2(x, s):
        x_20.append(s)
    if LOSS12(x, s):
        x_21.append(s)
print(min(x_19))
print(min(x_20), max(x_20))
print(min(x_21))