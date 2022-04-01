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
b=a[0]
c=a[1]
maxi=c+b
for i in range(n-1):
    summa=a[i] + a[i+1]
    if summa>maxi:
        maxi=summa
        b=a[i]
        c=a[i+1]
print(b,c)
