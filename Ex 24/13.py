f = open('24.txt')
a = f.readline()
a.split('XXZY')
count = 0
max_len = 0
print(len(max(a, key=len)))