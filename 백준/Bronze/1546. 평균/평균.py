a=int(input())
score=list(map(int,input().split()))
M=max(score)
l=[]

for i in range(0,a):
    l.append(score[i]/M*100)

ave=sum(l)/a

print(ave)