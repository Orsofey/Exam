f = open('web27.5.1B.txt')
n = int(f.readline())
sum_final = 0
min_razn = 1000000000
list_min_razn = []

for i in range(n):
    a, b = map(int, f.readline().split())
    abs(a - b)
    sum_final += max(a, b)
    if abs(a-b) < min_razn and abs(a-b) != 0 and abs(a-b) % 10 != 0:
        min_razn = abs(a-b)

if sum_final % 10 == 0:
    sum_final -= min_razn

print(sum_final)
