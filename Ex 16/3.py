def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * G(n) + 3*n

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) + 5*n
print(F(4) - G(5))