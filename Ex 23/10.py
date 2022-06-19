def map(start, end):
    if start == 20:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return map(start+1, end) + map(start*2, end) + map(start*3, end)
print(map(2, 25))