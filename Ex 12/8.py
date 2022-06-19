a = '2'*50 + '5'*30 + '6'*100
while '25' in a or '26' in a:
    if '25' in a:
        a = a.replace('25', '266', 1)
    else:
        a = a.replace('26', '66', 1)
print(a)
count = 0
for i in range(len(str(a))):
    if int(a[i]) == 6:
        count += 1
print(count)