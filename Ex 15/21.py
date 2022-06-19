def Del(n, m):
    return n % m == 0
#(ДЕЛ(x, 16) /\ ¬ДЕЛ(x, 64)) → ДЕЛ(x, A)

for A in range(1, 10000):
    A_true = True
    for x in range(1, 10000):
        if ((Del(x, 16) and (not(Del(x, 64)))) <= Del(x, A) ) == False:
            A_true = False
    if A_true == True:
        print(A)