a=int(input('Введи a:'))
k=0
for i in range(1, a+1):
    if a%i==0:
        k+=1
        print(i, end=' ')
print()
print('Количество делителей:', k)
