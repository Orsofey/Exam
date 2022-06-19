# ищем кол-во делителей числа
for n in range(100356, 100367+1):
    deliteli = []
    # проходимся до самого числа включительно(т.к. делители)
    for i in range(1, n+1):
        if n % i == 0:
            deliteli.append(i)
    if len(deliteli) == 4:
        print(deliteli)