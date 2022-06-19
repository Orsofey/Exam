for i in range(1, 1000):
    x = i
    L = 0
    M = 0
    while x > 0:
        L += 1
        M += (x % 10)
        x //= 10
    if L == 3 and M == 9:
        print(i)