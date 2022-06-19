for i in range(1, 10000):
    x = i
    Q = 38
    L = 0
    while x >= Q:
        L += 1
        x -= Q
    M = x
    if M < L:
        M = L
        L = x
    if L == 2 and M == 9:
        print(i)