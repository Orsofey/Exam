f = open('17.txt')
a = f.readline()

count = 1
max_len = 1
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        count += 1
        if max_len < count:
            max_len = count
    else:
        count = 1