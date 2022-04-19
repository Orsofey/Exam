f = open('24_1_5.txt')
s = f.readline()
a = s.split("K")
count = 0
z = []

for i in range(1, len(a)-1):
    if "L" not in a[i] and len(a[i]) >= 10:
        count += 1

z.sort(reverse=True)
print(count)