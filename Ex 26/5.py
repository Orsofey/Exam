f = open('26.5.txt')
N, M = map(int, f.readline().split())

izm = []
for s in f:
    izm.append(int(s))
    izm.sort(reverse=True)

win_izm = izm[0:M]
print(izm[:M], izm[M:M+10])
print(int(sum(win_izm)/len(win_izm)))

not_win_izm = izm[M+1:N]
print(max(not_win_izm))
