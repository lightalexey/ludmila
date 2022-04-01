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
summa = 0
p=1
k=0
sr=0
kpol=0
for i in range(n):
    summa += a[i]
    p *= a[i]
    if a[i]%2==0:
        k+=1
    if a[i]>0:
        sr += a[i]
        kpol +=1
sred=summa/n
print('Сумма всех элементов списка равна', summa)
print('Произведение всех элементов:', p)
print(sred)
print(k)
print(sr, kpol)
print(sr/kpol)
print(a[0])
print(a[-1])

