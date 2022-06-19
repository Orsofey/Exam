def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) + 3 * G(n - 1)

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) + 2 *G(n - 1)
for i in range(1, 10**10):
    if G(i) > 10**10:
        print(i)
        break