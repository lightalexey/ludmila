def F(n):
    if n<2:
        return 1
    if n>=2 and n%2==0:
        return F(n/2)+1
    else:
        return F(n-3)+3
for n in range(100000):
    if F(n)==31:
        print(n)