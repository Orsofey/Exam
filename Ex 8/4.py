from itertools import *
count = 0
for i in product('АКРУ', repeat=5):
    x = i
    count += 1
    if x[0] + x[1] + x[2] + x[3] + x[4] == 'РУКАК':
        print(count)