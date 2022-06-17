for x in range(1,100):
    xx=x
    a = 2*x - 91
    b = 3*x - 159
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a==15:
        print(xx)