from itertools import *

counttruevalue = 0
for i in permutations("ПИРОГ", r=4):
    if i[0] != "П" and "ГИ" not in "".join(i):
        counttruevalue += 1
print(counttruevalue)