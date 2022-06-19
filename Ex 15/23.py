def Del(n, m):
    return n & m
for A in range(1, 1000):
    A_true = True
    for x in range(1, 10000):
        if ( (x & A != 0) <= ((x & 12 == 0) <= (x & 39 != 0)) ) == False:
            A_true = False
    if A_true == True:
        print(A)