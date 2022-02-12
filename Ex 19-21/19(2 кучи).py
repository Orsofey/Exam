def WIN1(x, S):
    if (x + S) < 91 and ((x + 1 + S) >= 91 or (x*3 + S) >= 91 or (x + S*3) >= 91):
        return True
    return False
a = []
for S in range(1, 85):
    if WIN1(14, S):
        a.append(S)

print(min(a))