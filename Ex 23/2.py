def task23(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start+1, end) + task23(start+10, end)
print(task23(3, 35))