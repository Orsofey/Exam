for i in range(1, 10000):
    x = i
    x0 = x
    N = 0
    while x > 0:
        d = x % 6
        N = 10*N + d
        x //= 6
    N += x0
    if N > 23456:
        print(i)