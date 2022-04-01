from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    number = randrange(11) # [-50..50]
    a.append(number)
    print(a[i], end=' ')
print()
# код начинается отсюда...
b=0
for i in range(n-1):
    if a[i] + a[i+1]>a[b]+a[b+1]:
        b=i
print(a[b], a[b+1])
