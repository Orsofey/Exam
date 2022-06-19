for x in range(301, 1000):

    if len(bin(x)) % 2 == 0:
        a = x[0:len(bin(x))/2]
        b = x[(len(bin(x)+1)/2)]
        print(str(a)+str(b))
    elif len(bin(x)) % 2 != 0:
        print('da')