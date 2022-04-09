def func(x, y, A):
    return (((x < 7) <= (x * y <= A)) and ((y**2 < A) <= (y < 101)))

for A in range(1, 1000):
    if all([func(x, y, A) for x in range(1, 100) for y in range(1, 100)]):
        print(A)
        break