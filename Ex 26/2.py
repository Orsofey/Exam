f = open('26.2.txt')
a, b = map(int, f.readline().split())


izm = []
for s in f:
    izm.append(int(s))

izm.sort(reverse=True)
dost_izm = izm[0:b]
print(int(sum(dost_izm)/len(dost_izm)))

dost_two_izm = izm[b:b+b]
print(int(sum(dost_two_izm)/len(dost_two_izm)))
