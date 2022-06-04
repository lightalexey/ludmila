n=50
s=''
while n>0:
    s=str(n%4)+s
    n=n//4
print(s)
