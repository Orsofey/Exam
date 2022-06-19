def Del(n, m):
    return n % m == 0

for A in range(1, 10000):
    A_true = True
    for x in range(1, 1000):
        if ( (not(Del(x, A))) <= ((not(Del(x, 42))) and (not(Del(x, 36)))) ) == False:
            A_true = False
    if A_true == True:
        print(A)