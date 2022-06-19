
def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 + 3*F(n-1) / 3
    if n % 2 != 0 and n > 1:
        return 2*n + (F(n-1) + F(n-3) + 2)/3

print(F(30))