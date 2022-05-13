for a1000 in range(10):
    for a10 in range(10):
        s=int('12345'+str(a1000)+'6'+str(a10)+'8')
        if s%17==0:
            print(s,s//17)
print()
for a1000 in range(10):
    for a10 in range(10):
        s=123450000+a1000*1000+600+a10*10+8
        if s%17==0:
            print(s,s//17)