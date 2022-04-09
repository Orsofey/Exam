for A in range(1, 1000):
    A_true = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((9*x + y) < A) or ((x + 14*y) > 49) or ((x + y) < 25)) == False:
                A_true = False
                break
        if A_true == False:
            break
    if A_true == True:
        print(A)
        break