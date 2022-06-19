f = open('2.24.8.5_web.txt')

s = f.readline()
# print(ord('A))=65 до print(ord('Z'))=70

count = [0]*100
print(count)
for i in range(len(s)-1):
    if s[i+1] == 'Z':
        # ord - перевод из буквы в число
        # обращение по индексу буквы перед Z(изначально там 0)
        count[ord(s[i])] += 1
print(max(count))
print(count.index(max(count)))
# обратный возврат из числа в букву
print(chr(85))

