a = int(input('Введи число:'))
summa = 0
k = 0
b = a % 10
v = 0
while a != 0:
    summa += a % 10  # summa = summa + a % 10
    if a // 2 == 0:
        v += 1
    a //= 10  # a = a // 10
    k += 1
print('Сумма цифр числа равна', summa)
print('Количество разрядов:', k)
print('Крайний правый рзряд:', b)
print('Количество чётных цифр:', v)
