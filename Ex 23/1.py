# подсчет количества программ(путей)
def task23(start, end):
    # если начало больше конца, то невозможно попасть в конец
    if start > end:
        return 0
    # если конец равен концу
    if start == end:
        return 1
    # если начало меньше конца
    if start < end:
        # подсчет кол-ва программ(путей)
        return task23(start+1, end) + task23(start*3, end)


print(task23(1, 35))