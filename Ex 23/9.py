def map(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return map(start+1, end) + map(start*2, end)
print(map(1, 6)*map(6, 13))