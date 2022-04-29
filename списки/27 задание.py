from random import randrange
a = []
n = 4
print('Исходный список:')
for i in range(n):
    number = randrange(10)
    a.append(number)
    print(a[i], end=' ')
print()
k=0
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]%2==0 or a[j]%2==0:
            k+=1
print(k)