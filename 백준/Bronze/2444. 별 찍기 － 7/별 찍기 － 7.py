n=int(input())
a=1
b=2*n-3
for i in range(1,n+1):
    print(" "*(n-i)+"*"*a)
    a+=2
for j in range(1,n):
    print(" "*(j)+"*"*b)
    b-=2