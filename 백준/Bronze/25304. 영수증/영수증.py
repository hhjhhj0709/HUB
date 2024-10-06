a=int(input())
b=int(input())
p=0

for i in range(b):
    price,amount=map(int,input().split())
    p+=price*amount

if p==a:
    print("Yes")
else:
    print("No")