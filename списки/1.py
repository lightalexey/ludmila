a = []
n = int(input('Введи количество элементов:'))
for i in range(n):
    number = int(input('Введи целое число:'))
    a.append(number)
print('Исходный список:')
for i in range(n):
    print(a[i], end=' ')
print()
print(a)
print(*a)