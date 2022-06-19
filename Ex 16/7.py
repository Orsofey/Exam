def F(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return F(n/3) - 1
    if n >= 2 and n % 3 != 0:
        return F(n - 1) + 17
count = 0
for i in range(1, 100000):
    if F(i) == 43:
        count += 1
print(count )