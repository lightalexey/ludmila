f=open('107_17.txt')
a=[]
for s in f:
    a.append(int(s))
min21=100001
for i in range(len(a)):
    if a[i]%21==0:
        min21=min(min21, a[i])
k=0
maxn=0
for i in range(len(a)-1):
    if a[i]%min21==0 or a[i+1]%min21==0:
        k+=1
        maxn=max(maxn, a[i]+a[i+1])
print(k, maxn)