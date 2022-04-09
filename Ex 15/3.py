def Del(a, b):
    return a % b == 0

for A in range(1, 1000):
    A_true = True
    for x in range(1, 1000):
        if ( (Del(x, A) and (not(Del(x, 12)))) <= (not(Del(x, 18)) ) ) == False:
            A_true = False
    if A_true == True:
        print(A)
