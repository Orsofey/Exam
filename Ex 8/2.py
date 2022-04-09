from itertools import *

counttruevalue = 0
for i in product("МАСТЕР", repeat=5):
    if i.count("М") >= 2:
        counttruevalue += 1
print(counttruevalue)