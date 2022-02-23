f = open('web27.5.3B.txt')
n = int(f.readline())
sum_final = 0
min_razn = 1000000

for i in range(n):
    a, b = map(int, f.readline().split())
    if abs(a-b) < min_razn and abs(a-b) % 100 != 12 and abs(a-b) != 0:
        min_razn = abs(a-b)
    sum_final += max(a, b)

if sum_final % 16 == 12:
    sum_final -= min_razn

print(sum_final)