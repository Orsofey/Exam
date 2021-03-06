# Победа за один ход
def WIN1(s):
    # Если позиция выигрышная, возвращает True
    return s + 3 >= 56 or s*2 >= 56

for s in range(1, 53):
    # Ищем позицию, которую может сделать Петя для победы Вани
    # Для Вани(он должен победить, поэтому проверяем их)
    if WIN1(s+3) or WIN1(2*s):
        print(s)
        break