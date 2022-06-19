f = open('file.txt')
max_dist = 0
for s in f:
    if s.count('a') < 20:
        for bukva in s:
            z = s.rindex(bukva) - s.index(bukva)
            if z > max_dist:
                max_dist = z