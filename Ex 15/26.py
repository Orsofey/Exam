for A in range(1, 10000):
    A_true = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ( (2*x - y < A) or ( (x > 55) or (y > 32)) ) == False:
                A_true = False
                break
        if A_true == False:
            break
    if A_true == True:
        print(A)