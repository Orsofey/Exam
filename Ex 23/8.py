def task23(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start+2, end) + task23(start*2, end)

print(task23(1, 26))