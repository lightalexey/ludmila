for n in range(1, 100):
    b = bin(n)[2:]
    b = b + str((b.count('1'))%2)
    b = b + str((b.count('1'))%2)
    if int(b, 2) > 97:
        print(int(b, 2), n)
