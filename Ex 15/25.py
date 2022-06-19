# на графики
for A in range(1, 1000):
    A_true = True
    for x in range(1, 10000):
        for y in range(1, 10000):
            if ((3*y - x < A) or (x >= 35) or (y >= 51)) == False:
                A_true = False
                break
        break
    if A_true == True:
            print(A)