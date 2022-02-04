a = int(input('Введи a='))
b = int(input('Введи b='))
c = int(input('Введи c='))
if a < b + c:
    if b < a + c:
        if c < a + b:
            print('Треугольник существует')
        else:
            print('Треугольник не существует')
    else:
        print('Треугольник не существует')
else:
    print('Треугольник не существует')
