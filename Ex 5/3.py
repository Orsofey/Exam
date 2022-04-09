def calculatorr(n):
    n_2 = bin(n)[2:]
    if bin(n)[2:].count("1") % 2 == 0:
        n_2 += "0"
    else:
        n_2 += "1"
    if n_2.count("1") % 2 == 0:
        n_2 += "0"
    else:
        n_2 += "1"
    return int(n_2, 2)

a = []
for n in range(1, 100):
    if calculatorr(n) < 268:
        a.append(calculatorr(n))

print(max(a))