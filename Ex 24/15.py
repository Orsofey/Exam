f = open('24.txt')
s = f.readline()

count = 1
max_len = 1
for i in range(len(s)):
    if s[i] in "AEOI" and s[i+1] in "AEOI" and s[i] <= s[i+1]:
        count += 1
        if max_len < count:
            max_len = count
