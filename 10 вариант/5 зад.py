for n in range(1, 256):
    b = bin(n)[2:]
    z=(8-int(len(b)))*'0'
    b =z+b
    b=b.replace('1','2')
    b=b.replace('0','1')
    b=b.replace('2','0')
    b=int(b, 2)
    b=b-n
    if b==113:
        print(n)