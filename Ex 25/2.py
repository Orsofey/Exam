# ищем кол-во делителей числа
for n in range(100356, 100367+1):
    deliteli = []
    # если из числа нельзя извлечь корень, то проверяем след n
    # потому получается четное число делителей, а надо нечет
    if n**0.5 % 1 != 0:
        continue
    for i in range(1, n+1):
        if n % i == 0:
            deliteli.append(i)
    if len(deliteli) == 4:
        print(deliteli)