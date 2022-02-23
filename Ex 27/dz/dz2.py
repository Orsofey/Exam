f = open('27.5.2A.txt')
n = int(f.readline())
sum_final = 0
min_razn = 10000000

for i in range(n):
    a, b = map(int, f.readline().split())
    if abs(a-b) < min_razn and abs(a-b) % 73 != 0 and abs(a-b) != 0:
        min_razn = abs(a-b)
    sum_final += min(a, b)

if sum_final % 73 == 0:
    sum_final += min_razn

print(sum_final)

f = open('27.5.2B.txt')
n = int(f.readline())
sum_final = 0
min_razn = 10000000

for i in range(n):
    a, b = map(int, f.readline().split())
    if abs(a-b) < min_razn and abs(a-b) % 73 != 0 and abs(a-b) != 0:
        min_razn = abs(a-b)
    sum_final += min(a, b)

if sum_final % 73 == 0:
    sum_final += min_razn

print(sum_final)