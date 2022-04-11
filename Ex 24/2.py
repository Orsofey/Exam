f = open('24_3_web.txt')
s = f.readline()
# заменяем C на E, чтобы потом исп. split только для E
s = s.replace("C", "E")
a = s.split("E")

print(len(max(a, key=len)))

max_len = 0
for i in range(len(a)):
    if len(a[i]) > max_len:
        max_len = len(a[i])
print(max_len)