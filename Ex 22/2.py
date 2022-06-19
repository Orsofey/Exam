for i in range(1, 1000):
    x = i
    L = x
    M = 98
    if L % 12 == 0:
        M = 24
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    if M == 14 and i > 100:
        print(i)