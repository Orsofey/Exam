f = open('26.4.txt')
N, M = map(int, f.readline().split())

izm = []
for s in f:
    izm.append(int(s))
    izm.sort(reverse=True)

opportunity = izm[0:882]
print(izm[M:M+10])

print((sum(opportunity)/len(opportunity)))

print(izm[M+1])