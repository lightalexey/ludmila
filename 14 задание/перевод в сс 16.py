a=10
ss=16
result=''
while a>0:
    number=str(a%ss)
    if number=='10':
        number='A'
    if number=='11':
        number='B'
    if number=='12':
        number='C'
    if number=='13':
        number='D'
    if number=='14':
        number='E'
    if number=='15':
        number='F'
    result=number+result
    a//=ss
print(result)