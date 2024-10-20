area=[[0] *100 for i in range(100)]

n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    
    for i in range(x,x+10):
        for j in range(y,y+10):
            area[i][j]=1

a=0

for i in range(100):
    for j in range(100):
        if area[i][j]==1:
            a+=1


print(a)