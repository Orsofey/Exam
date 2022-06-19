P = list(range(55, 81))
Q = list(range(20, 106))
A = []
for x in range(1, 1000):
    if ( (x in Q) <= (((x in P) == (x in Q)) or ((not(x in P)) <= (x in A)))) == False:
        A.append(x)
print(len(A))
print(max(A) - min(A))