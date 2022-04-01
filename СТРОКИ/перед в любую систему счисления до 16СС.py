a = int(input())
b = int(input())
k=''
while a != 0:
    k=k+str(a%b)
    a //= b
print(k[::-1])
