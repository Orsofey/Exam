for i in range(1, 1000):
    s = i
    n = 4
    while s <= 96:
        s += 8
        n += 5
    if n == 54:
        print(i)