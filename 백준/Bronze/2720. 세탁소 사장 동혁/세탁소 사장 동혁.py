n=int(input())

for i in range(n):
    z=int(input())
    a=z//25
    b=(z-a*25)//10
    c=(z-a*25-b*10)//5
    d=(z-a*25-b*10-c*5)//1
    print(a,b,c,d)
