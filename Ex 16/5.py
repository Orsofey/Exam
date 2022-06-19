def F(n):
    if n == 0:
        return 0
    if n % 3 == 2 and n > 0:
        return F(n-1) + 1
    if n % 3 < 2 and n > 0:
        return F((n-n%3)/3)

for i in range(1, 10000):
    if F(i) == 5:
        print(i)
        break