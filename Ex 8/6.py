from itertools import *
count = 0
for i in permutations('ЗЛОЙ', r=4):
    if 'Й' not in i[0] and 'ОЙ' not in ''.join(i):
        count += 1
print(count)