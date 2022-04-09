def func(x, y, A):
    return ((x >= 46) or (x < 9*y) or (y*x < A))

for A in range(1, 1000):
    if all([func(x, y, A) for x in range(1, 1000) for y in range(1, 1000)]):
        print(A)
        break