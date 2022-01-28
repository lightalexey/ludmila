a = int(input('Введи a='))
b = int(input('Введи b='))
c = int(input('Введи c='))
if a>b and a>c:
    print(a)
if b>a and b>c:
    print(b)
if c>a and c>b:
    print(c)

print(max(a, b, c))