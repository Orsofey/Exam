f = open('24_7_web.txt')
s = f.readline()
s = s.replace('AB', 'BA')
a = s.split('BA')
print(len(max(a, key=len))+2)