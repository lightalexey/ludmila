a = input('Введи число:')
summa = 0
v = 0
for i in range(len(a)):
    summa += int(a[i])
    if int(a[i]) // 2 == 0:
        v += 1
print('Сумма цифр числа равна:', summa)
print('Количество разрядов:', len(a))
print('Крайний правый рзряд:', a[-1])
print('Количество чётных цифр:', v)
