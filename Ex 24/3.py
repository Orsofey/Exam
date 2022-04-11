f = open('24_4_web.txt')
s = f.readline()
a = s.split("Y")

max_len = 0
for i in range(len(a)-1):
    if len(a[i] + a[i+1]) + 1 > max_len:
        max_len = len(a[i] + a[i+1]) + 1

print(max_len)