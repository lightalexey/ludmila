a = int(input('Введи число:'))
summa = 0
while a != 0:
    summa += a % 10  # summa = summa + a % 10
    a //= 10  # a = a // 10
print('Сумма цифр числа равна', summa)