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
maximum=a[0]
minimum=a[0]
imax=0
imin=0
for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
        imax=i
    if a[i] < minimum:
        minimum = a[i]
        imin=i
print(maximum, imax)
print(minimum, imin)