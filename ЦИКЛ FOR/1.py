k = 0
k2=0
k3=0
k4=0
for i in range(10, 99+1):
    print(i, end=' ')
<<<<<<< HEAD
    k += 1  # k = k + 1 k++
=======
    k+=1
    if i%2==0:
        k2+=1
    if i%3==0:
        k3+=1
    if i%2==0 and i%3==0:
        k4+=1
>>>>>>> cd4ea719d235bf49c7f2f957a43fb0f115c6448a
print()
print('Количество двухзначных чисел равно', k)
print('Количество чётных чисел:', k2)
print('Количество чисел кратных трём:', k3)
print ('Количество чисел кратных 2 и 3:', k4)