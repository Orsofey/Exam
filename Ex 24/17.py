f = open('24.txt')
count = 0
for s in f:
    if s.count('AB') >= s.count("C") and s.count("AB") > 1 and s.count("C") > 1:
        count += 1