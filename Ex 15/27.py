for A in range(1, 10000):
    A_true = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((10*x - y + 37 != 0) or (A < x) or (A < y)) == False:
                A_true = False
                break
        if A_true == False:
            break
    if A_true == True:
        print(A)