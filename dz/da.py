
Q = list(range(12, 92))
P = list(range(10, 52))
A = []

for x in range(1, 1000):
    if ( (x in A) or ((not(x in P)) <= (not(x in Q))) ) == False:
        A.append(x)

print(max(A)-min(A))