def Del(n, m):
    return n % m == 0

true_A = []
for A in range(1, 1000):
    for x in range(1, 1000):
        if ((x & 76 != 0) <= ((x & 38 == 0) <= (x & A != 0))) == False:
            break
    else:
        true_A.append(A)

print('минимальный А =', min(true_A))
print('максимальный А =', max(true_A))