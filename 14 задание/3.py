a=9**8+3**5-9
k=0
while a>0:
    if a%3==2:
        k+=1
    a//=3
print(k)