x=9**18+3**54-9
s=''
while x>0:
    s+=str(x%3)
    x//=3
print(s.count('2'))

x=9**18+3**54-9
s=0
while x>0:
    if x%3==2:
        s+=1
    x//=3
print(s)