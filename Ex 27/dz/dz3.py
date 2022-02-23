f = open('27.5.3A.txt')
n = int(f.readline())
sum_final = 0
min_razn = 100000

for i in range(n):
    a, b = map(int, f.readline().split())
    if abs(a-b) % 16 != 14 and abs(a-b) != 0 and abs(a-b) < min_razn:
        min_razn = abs(a-b)
    sum_final += max(a, b)

if sum_final % 16 == 14:
    sum_final -= min_razn

print(sum_final)

f = open('27.5.3B.txt')
n = int(f.readline())
sum_final = 0
min_razn = 100000

for i in range(n):
    a, b = map(int, f.readline().split())
    if abs(a - b) % 16 != 14 and abs(a - b) != 0 and abs(a - b) < min_razn:
        min_razn = abs(a - b)
    sum_final += max(a, b)

if sum_final % 16 == 14:
    sum_final -= min_razn

print(sum_final)