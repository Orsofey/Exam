def Del(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_true = True
    for x in range(1, 1000):
        if ( (not(Del(x, A))) <= ( (Del(x, 20) <= (Del(x, 40)))) ) == False:
            A_true = False
            break
    if A_true == True:
        print(A)