# stroka = input('Введи строку:')
stroka = 'Мама мыла раму!'
n = len(stroka)
print('Количество символов:', n)
print('Первый символ:', stroka[0])
print('1 способ. Последний символ:', stroka[n-1])
print('2 способ. Последний символ:', stroka[-1])
k_a = 0
for i in range(n):
    if stroka[i] == 'а':
        k_a += 1
print('1 способ. Количество букв а:', k_a)
print('2 способ. Количество букв а:', stroka.count('а'))
print('Первое слово:', stroka[0:4])
# stroka[0] = 'м' строку изменить нельзя!!!
stroka = stroka.replace('М', 'м')
print(stroka)
stroka = stroka.replace('мама мыла', 'папа мыл')
print(stroka)
stroka = stroka.replace('п', 'П', 1)
print(stroka)
if 'Папа' in stroka:
    print('Слово Папа есть в строке')