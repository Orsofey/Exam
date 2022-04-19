f = open('2.24.8.4_web.txt')
s = f.readline()
max_len = 0
count = 1
for i in range(len(s)-1):
    # if s[i:i+2].isdigit() and (int(s[i]) + int(s[i+1]) % 2 != 0
    if (s[i] in "02468" and s[i+1] in "13579") or (s[i] in "13579" and s[i+1] in "02468"):
        count += 1
        max_len = max(count, max_len)
    else:
        count = 1

print(max_len)