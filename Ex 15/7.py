def Del(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_true = True
    for x in range(1, 10000):
        if ( (Del(x, A) and Del(x, 36)) <= (Del(x, 6) and (Del(x, 120))) ) == False:
            A_true = False
            break
    if A_true == True:
        print(A)
        break