from itertools import *

countvalue = 0
for i in product("ВЕСНА", repeat=4):
    if i[0] != "А" and i[-1] != "С" and i.count('В') == 1:
        countvalue += 1
print(countvalue)