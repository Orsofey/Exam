def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n/2)
    if n % 2 != 0:
        return 1 + F(n-1)

for i in range(1, 10000):
    if F(i) == 12:
        print(i)