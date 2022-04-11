f = open("24_5_web.txt")
s = f.readline()
cnt = 0
a = s.split("E")

for i in range(1, len(a)-1):
    if len(a[i]) >= 12 and "Z" not in a[i]:
        cnt += 1
print(a)
print(cnt)