Q = list(range(18, 42))
P = list(range(9, 18))
A = []
for x in range(1, 100):
    if (((x in P) or (x in Q)) <= (x in A)) == False:
        A.append(x)
print(max(A)-min(A))