a=10
ss=16
result=''
alf='0123456789ABCDEF'
while a>0:
    number=alf[a%ss]
    result=number+result
    a//=ss
print(result)
print(int(result,ss))