f = open('web27.5.1A.txt')
# считываем количество строк ценами
n = int(f.readline())
sum_final = 0


for i in range(n):
    # разделение одной строчки на список из превой цены и второй
    # Первый способ
    s = f.readline().split()
    a = int(s[0])
    b = int(s[1])

    #Второй способ
    a, b = map(int, f.readline().split())

    sum_final += max(a, b)

print(sum_final)





