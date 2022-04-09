for A in range(1, 1000):
    for x in range(1, 10000):
        if ((x & 18 == 0) or (x & 37 != 0) or (x & A) != 0) == False:
            break
    else:
        print(A)