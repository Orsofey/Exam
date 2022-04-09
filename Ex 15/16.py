count = 0
for A in range(1, 1000):
    A_true = True
    for x in range(1, 100):
        for y in range(1, 100):
            if (((x > 34) <= ((x*y + 9*x) >= A)) and (((y*x + y)>A) <= (y>=2))) == False:
                A_true = False
                break
        if A_true == False:
            break
    if A_true == True:
        count += 1
print(count)