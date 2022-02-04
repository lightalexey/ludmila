a = int(input('Введи a='))
b = int(input('Введи b='))
c = int(input('Введи c='))
if a < b + c and b < a + c and c < a + b:
    # print('Треугольник существует')
    if a == b == c:
        print('Треугольник равносторонний')
    else:
        if a == b or b == c or c == a:
            print('Треугольник равнобедренный')
        else:
            if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
                print('Треугольник прямоугольный')
            else:
                print('Треугольник произвольный')
else:
    print('Треугольник не существует')
