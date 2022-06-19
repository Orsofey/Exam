a = '1'*10 + '2'*20 + '3'*30

while '1' in a or '2' in a or '3' in a:
    if '1' in a:
        a = a.replace('1', '22')
    if '2' in a:
        a = a.replace('2', '2')
    if '3' in a:
        a = a.replace('3', '1')
        
print(a)