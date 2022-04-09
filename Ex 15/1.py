def Del(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_true = True
    for x in range(1, 1000):
        if (Del(x, A) <= (Del(x, 3) and Del(x, 10))) == False:
            A_true = False
            break
    if A_true == True:
        print(A)