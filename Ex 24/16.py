f = open('24.txt')
s = f.readline()

max_len = 0
count = 0
for i in range(len(s)):
    if s[i] in '02468':
        count += 1
    else:
        count = 0
    if s[i] == '0':
        max_len = max(max_len, count)