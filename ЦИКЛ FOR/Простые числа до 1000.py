for a in range(2, 1000 + 1):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k += 1
    if k == 0:
        print(a)
