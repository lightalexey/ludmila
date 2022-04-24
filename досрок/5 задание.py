for n in range(1,100):
    if n%2==0:
        b=bin(n)[2::]+'10'
    else:
        b='1'+bin(n)[2::]+'01'
    if int(b,2)>516:
        print(int(b,2), n)
