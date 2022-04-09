def calculator(n):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = n2 + n2[0] + n2[1]
    else:
        n2 = '1' + n2 + '0'
    return int(n2, 2)


a = []
for n in range(1, 1000):
    if calculator(n) > 320:
        a.append(calculator(n))

print(min(a))