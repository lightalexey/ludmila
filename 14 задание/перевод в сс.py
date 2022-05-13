a=1560
ss=8
result=''
while a>0:
    result+=str(a%ss)
    a//=ss
print(result[::-1].count('3'))