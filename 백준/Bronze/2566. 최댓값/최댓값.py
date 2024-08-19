num=[]
ma=0
a=0
b=0
for i in range(9):
    num.append(list(map(int,input().split())))
for i in range(9):
    for j in range(9):
        if ma<num[i][j]:
            ma=num[i][j]
            a=i
            b=j
print(ma)
print(a+1,b+1)