text=input()
al=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in al:
    if i in text:
        print(text.index(i),end=" ")
    else:
        print("-1",end=" ")