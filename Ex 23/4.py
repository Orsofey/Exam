def task23(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return task23(start+2, end) + task23(start*2, end) + task23(start*2 + 1, end)

print(task23(2, 45))