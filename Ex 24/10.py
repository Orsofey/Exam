f = open('2.24.8.5_web.txt')
s = f.readline()
cur_len = 0
max_cur_len = 0
for i in range(len(s)):
    if s[i] in "2468":
        cur_len += 1
    elif s[i] == "0":
        cur_len += 1
        max_cur_len = max(cur_len, max_cur_len)
    else:
        cur_len = 0
print(max_cur_len)