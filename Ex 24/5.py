f = open('24_6_web.txt')
s = f.readline()
a = s.split("XXZY")
print(len(max(a, key=len))+6)
print(a.index(max(a, key=len)))
print(len(a))