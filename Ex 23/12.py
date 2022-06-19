def map(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    if start > end:
        return map(start-1, end) + map(start-3, end) + map(start//3, end)
print(map(22, 2))