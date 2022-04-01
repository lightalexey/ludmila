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

