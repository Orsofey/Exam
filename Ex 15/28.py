for A in range(1, 1000):
    A_true = False
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ( (x*y > A) and (x > y) and (x < 8)) == True:
                A_true = True
                break
        if A_true == True:
            break
    if A_true == False:
        print(A)