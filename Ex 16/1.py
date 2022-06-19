def F(n):
    if n == 0:
        return 0
    if n >= 1:
        return F(n-1) + n
print(F(10))