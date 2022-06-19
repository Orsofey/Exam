from itertools import *

count = 0
for i in product('АБВГДЕЖЗИК', repeat=3):
    count += 1
    if 'АЖЕ' == ''.join(i):
        print(count)