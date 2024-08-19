N,M=map(int,input().split())
num1=[]
num2=[]
for i in range(N):
    a=list(map(int,input().split()))
    num1.append(a)
for i in range(N):
    b=list(map(int,input().split()))
    num2.append(b)

for i in range(N):
    for j in range(M):
        print(num1[i][j]+num2[i][j],end=" ")
    print()