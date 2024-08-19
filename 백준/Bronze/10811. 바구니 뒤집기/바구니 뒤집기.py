ba,n=map(int,input().split())
basket=[]

for i in range(1,ba+1):
    basket.append(i)

for j in range(n):
    a,b=map(int,input().split())
    basket2=list(basket[a-1:b])
    basket2.reverse()
    basket[a-1:b]=basket2
    
print(*basket)