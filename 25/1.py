for i in range(350000, 400000):
    for n in range(2, i // 2 + 1):
        if i%n==0:
            min = n
            break
    for n in range(i // 2, 1, -1):
        if i%n==0:
            max = n
            break
    M = max-min
    if M % 23 == 9:
        print(i)