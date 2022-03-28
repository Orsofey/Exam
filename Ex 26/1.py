f = open('26.1.txt')
N, K = map(int, f.readline().split())
izm = []

for s in f:
    izm.append(int(s))
    izm.sort(reverse=True)

dost_izm = izm[K:-K]
print(min(dost_izm), int(sum(dost_izm)/len(dost_izm)))