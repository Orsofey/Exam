f = open('2.24.8.2_web.txt')
s = f.readline()
a = []
count = 1
for i in range(len(s)-1):
    if s[i] >= s[i+1] > '5':
        count += 1
        a.append(count)
    else:
        count = 1
print(max(a))