f = open('24_1_web.txt')
s = f.readline()

# разделение на последовательности без Y
a = s.split("Y")
# максимальная по длине последовательность символов без Y
print(len(max(a, key=len)))

max_len = 0
for i in range(len(a)):
    if len(a[i]) > max_len:
        max_len = len(a[i])

print(max_len)