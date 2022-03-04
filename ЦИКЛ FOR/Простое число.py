a = int(input('Введи a:'))
k = 0
for i in range(2, a//2+1):
    if a%i==0:
        k += 1
if k!=0:
    print('Число составное')
else:
    print('Число простое')
