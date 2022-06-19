value = '2' + 81*'5'

while '25' in value or '355' in value or '4555' in value:
    if '25' in value:
        value = value.replace('25', '4', 1)
    if '355' in value:
        value = value.replace('355', '2', 1)
    if '4555' in value:
        value = value.replace('4555', '3', 1)
print(value)