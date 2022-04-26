def task23(start, end):
    if start == 26:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    return task23(start+2, end) + task23(start*2, end)

print(task23(2, 14)*task23(14, 56))