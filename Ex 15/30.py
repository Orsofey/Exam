Q = list(range(18, 33))
P = list(range(5, 21))
A = list(range(0, 1000))

for x in range(0, 1000):
    if ( ((x in A) <= ((x in P))) or (x in Q)) == False:
        A.remove(x)
print(A)
print(max(A)-min(A))