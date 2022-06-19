a = 9*'8' + 12*'5'

while '555' in a or '888' in a:
    while '555' in a:
        a = a.replace('555', '8', 1)
    while '888' in a:
        a = a.replace('888', '5', 1)
print(a)