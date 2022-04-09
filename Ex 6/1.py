g = []
for i in range(1, 10000):
    s = i
    n = 2
    while s < 150:
        s = s + 10
        n = n * 5
    if n == 250:
        g.append(i)

print(max(g))