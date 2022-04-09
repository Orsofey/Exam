def calculator(n):
    a = 0
    # считаем сумму четных цыфр
    for i in str(n):
        if int(i) % 2 == 0:
            a += int(i)
    b = 0
    # вычисление cуммы цифр, стоящих на четных индексах
    for i in range(1, len(str(n)), 2):
        b += int(str(n)[i])
    return abs(a-b)

for n in range(2, 1000):
    if calculator(n) == 13:
        print(n)