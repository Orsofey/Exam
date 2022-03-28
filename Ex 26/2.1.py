f = open('26.web_2.txt')
M, N = map(int, f.readline().split())

items = []
for s in f:
    items.sort()
    items.append(int(s))

count = 0
items_in_train = []
for i in range(len(items)):
    if sum(items_in_train) + items[i] <= M:
        items_in_train.append(items[i])
    elif sum(items_in_train) - items_in_train[-1] + items[i] <= M:
        del items_in_train[-1]
        items_in_train.append(items[i])
    else:
        count += 1

print(count)
print(len(items_in_train))