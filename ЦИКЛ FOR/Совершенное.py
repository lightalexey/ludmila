a=int(input('Введи a:'))
summa=0
for i in range(1, a):
    if a%i==0:
        summa+=i
if a==summa:
    print('Да, число совершенное')
else: 
    print('Нет, число несовершенное')
