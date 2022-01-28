a = int(input('Введи a='))
b = int(input('Введи b='))
c = int(input('Введи c='))
D = b**2-4*a*c
if D<0:
    print('Нет действительных решений')
if D == 0:
    x = -b/2/a
    print(x)
if D>0:
    x1 = (-b+D**(1/2))/(2*a)
    x2 = (-b-D**(1/2))/(2*a)
    print(x1,x2)
