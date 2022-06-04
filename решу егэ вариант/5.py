for n in range(1, 100):
    b=bin(n)[2:]
    if n%2==0:
        b='1'+b+'0'
    else:
        b='11'+b+'11'
    if int(b,2)>52:
        print(n)
