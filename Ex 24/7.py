f = open('2.24.8.1_web.txt')
s = f.readline()
count = 0
a = []
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
    else:
        a.append(count)
        count = 1

print(print(max(a)))