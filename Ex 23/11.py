def map(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    if start > end:
        return map(start-2, end) + map(start-5, end)
print(map(27, 2))