s='1'*51 +'2'*29+'3'*23
while '201' in s or '10'in s or '2302' in s:
    s=s.replace('201','03', 1)
    s=s.replace('10', '02', 1)
    s=s.replace('2302', '01', 1)
print(s)