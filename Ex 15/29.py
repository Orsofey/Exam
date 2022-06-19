R = list(range(30, 51))
Q = list(range(4, 16))
P = list(range(10, 41))
A = []
for x in range(1, 100):
    if (((x in A) or (x in P)) or ((x in Q) <= (x in R))) == False:
        A.append(x)
print(A)
# длина равна 10-4, 10, потому что в условии 10, 4, потому что в условии 4
print(len(A))