from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    number = randrange(1000)
    a.append(number)
    print(a[i], end=' ')
print()
k=0
for i in range(n-1):
    if a[i]>9 and a[i]<100 or a[i+1]>9 and a[i+1]<100:
        k+=1
print(k)
