l=[]
for i in range(9):
    a=int(input())
    l.append(a)

M=max(l)

print(M)
index=l.index(M)
print(index+1)