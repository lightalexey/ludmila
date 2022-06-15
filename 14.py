x=(103*7**103)-(5*7**57)+98
summa=0
while x>0:
    summa+=x%7
    x=x//7
print(summa)
