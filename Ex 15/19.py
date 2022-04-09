Q = list(range(15, 40))
P = list(range(10, 18))
A = list(range(1, 100))
for x in range(1, 100):
    if (((x in Q) <= (x in P)) <= (not(x in A))) == False:
        A.remove(x)

print(max(A)-min(A))