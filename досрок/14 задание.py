nn = n=((3*16**2018)-(2*8**1028)-(3*4**1100)-(2**1050)-2022)
a=''
while n>0:
    a=str(n%4)+a
    n=n//4
# print(a)
k=0
for i in range(len(a)):
    if a[i]=='3':
        k+=1
print(k)
# еще способ
k = 0
while nn > 0:
    if nn % 4 == 3:
        k += 1
    nn //= 4
print(k)