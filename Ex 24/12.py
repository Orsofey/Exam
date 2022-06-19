f = open('24.txt')
s = f.readline()
a = s.split("Y")
print(a)
max_len = 0
for i in range(len(a)-1):
    if len(a[i]) + len(a[i+1]) + 1 > max_len:
        max_len = len(a[i]) + len(a[i+1]) + 1
print(max_len)
