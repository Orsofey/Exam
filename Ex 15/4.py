def Del(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_true = True
    for x in range(1, 1000):
        if ((not(Del(x, 7)) or not(Del(x, 15))) <= (not(Del(x, A)))) == False:
            A_true = False
    if A_true == True:
        print(A)
