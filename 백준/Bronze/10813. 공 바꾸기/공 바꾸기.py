N,M=map(int,input().split())
ba=list()

for i in range(1,N+1):
    ba.append(i)

for i in range(M):
    a,b=map(int,input().split())
    temp=ba[a-1]
    ba[a-1]=ba[b-1]
    ba[b-1]=temp

print(*ba)