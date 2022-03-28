f = open('26.3.txt')
N, K, M = map(int, f.readline().split())

izm = []
for s in f:
    izm.append(int(s))
    izm.sort(reverse=True)

win_izm = izm[0:K]
prizer_izm = izm[K:K+M]

print(min(win_izm))
print(int(sum(prizer_izm)/len(prizer_izm)))