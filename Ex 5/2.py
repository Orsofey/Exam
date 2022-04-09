def calculater(n):
    # 1
    n_2 = bin(n)[2:]
    # 2
    n_2 += n_2[-1]
    # 3
    if bin(n)[2:].count('1') % 2 == 0:
        n_2 += "0"
    else:
        n_2 += "1"
    # 4
    if n_2.count("1") % 2 == 0:
        n_2 += "1"
    else:
        n_2 += "0"
    return int(n_2, 2)


for n in range(1, 100):
    if calculater(n) > 55:
        print(n)
        break


print(calculater(7))