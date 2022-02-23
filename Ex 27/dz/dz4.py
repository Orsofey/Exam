f = open('27.5.4A.txt')
n = int(f.readline())
sum_final = 0
min_razn = 1000000

for i in range(n):
    a, b, c = map(int, f.readline().split())
    z = [a, b, c]
    z.sort()
    if abs(z[2] - z[0]) < min_razn and abs(z[2] - z[0]) % 60 != 0:
        min_razn = abs(z[2] - z[0])
    if abs(z[2] - z[1]) < min_razn and abs(z[2] - z[1]) % 60 != 0:
        min_razn = abs(z[2] - z[1])
    sum_final += z[0] + z[1]

if sum_final % 60 == 0:
    sum_final += min_razn

print(sum_final)

f = open('27.5.4B.txt')
n = int(f.readline())
sum_final = 0
min_razn = 1000000

for i in range(n):
    a, b, c = map(int, f.readline().split())
    z = [a, b, c]
    z.sort()
    if abs(z[2] - z[0]) < min_razn and abs(z[2] - z[0]) % 60 != 0:
        min_razn = abs(z[2] - z[0])
    if abs(z[2] - z[1]) < min_razn and abs(z[2] - z[1]) % 60 != 0:
        min_razn = abs(z[2] - z[1])
    sum_final += z[0] + z[1]

if sum_final % 60 == 0:
    sum_final += min_razn

print(sum_final)