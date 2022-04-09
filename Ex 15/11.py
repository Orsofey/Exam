a = []

for A in range(1, 1000):
    A_true = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x > 42) or (y < x) or (3*x < A)) == False:
                A_true = False
                break
        if A_true == False:
            break
    if A_true == True:
        print(A)
        break
