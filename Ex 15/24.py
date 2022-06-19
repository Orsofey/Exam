def Del(n, m):
    return n & m

for A in range(1, 10000):
    A_true = True
    for x in range(1, 10000):
        if ( (x & A != 0) <= (((x & 76 == 0) or (x & 45 == 0)) <= (x & 22 != 0))) == False:
            A_true = False
    if A_true == True:
        print(A)