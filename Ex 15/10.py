a = []

for A in range(1, 100):
    A_true = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((y - 15*x) < A) or (x > 99) or (y > 64)) == False:
                A_true = False
                break
        if A_true == False:
            break
    if A_true == True:
        a.append(A)

print(min(a))