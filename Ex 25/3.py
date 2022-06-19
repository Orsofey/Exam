# ищем кол-во делителей числа
n = 700001
count = 0
while count != 6:
    F = 0
    for i in range(2, n):
        if n % i == 0:
            # МАксимальный делитель минус минимальный
            F = n // i - i
            break
    if F != 0 and F % 11 == 0:
        print(n, F)
        count += 1
    n += 1