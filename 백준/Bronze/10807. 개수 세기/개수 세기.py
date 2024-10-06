n=int(input())
m=list(map(int,input().split()))
v=int(input())
num=0

for i in range(n):
    if v==m[i]:
        num+=1

print(num)