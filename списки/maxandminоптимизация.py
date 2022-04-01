from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    number = randrange(101) - 50 # [-50..50]
    a.append(number)
    print(a[i], end=' ')
print()
# код начинается отсюда...
imax=0
imin=0
for i in range(n):
    if a[i] > a[imax]:
        imax=i
    if a[i] < a[imin]:
        imin=i
print(a[imax], imax)
print(a[imin], imin)