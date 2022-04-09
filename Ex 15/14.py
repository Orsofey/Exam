def formule(x, y, A):
    return (((y + 5 * x != 31) or (A > x - 2)) and (A < y + 37))

for A in range(1, 1000):
    if all([formule(x, y, A) for x in range(1, 1000) for y in range(1, 1000)]):
        print(A)
        break