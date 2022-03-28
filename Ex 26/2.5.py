f = open('26.web_5.txt')
n = int(f.readline())
all_elements = []
elements_more_than_120 = []

for s in f:
    all_elements.append(int(s))
    if int(s) > 120:
        elements_more_than_120.append(int(s))

elements_more_than_120.sort()
print(sum(all_elements)-sum((elements_more_than_120[0:len(elements_more_than_120)//2]))*0.25, max(elements_more_than_120[0:len(elements_more_than_120)//2]))
