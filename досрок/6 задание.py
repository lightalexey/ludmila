s=int(input())
s=(s-10)//7
n=1
while s>0:
    n=n*2
    s=s-n
print(n)
