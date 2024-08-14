N,M=map(int,input().split())

result=[]
for i in range(N):
    result.append(0)

for i in range(M):
    start,end,number=map(int,input().split())
    for j in range(start-1,end):
        result[j]=number

print(*result)